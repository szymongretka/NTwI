from typing import List, MutableSet, Generator, Tuple, Dict
import string
from itertools import chain, groupby, product
from collections import Counter, defaultdict
from core.granulation.granule import Granule
from core.tokenization.word_token import WordToken
import nltk
from core.filter.filter_stop_words import ignorable_tokens


class RAKEKeywordsSearcher(object):
    """
    Class for performing `Rapid Automatic Keyword Extraction Algorithm`:
    https://www.researchgate.net/publication/227988510_Automatic_Keyword_Extraction_from_Individual_Documents
    """

    def __init__(self, lang='english', min_length=1, max_length=10):
        self.__lang = lang
        self.__min_length = min_length
        self.__max_length = max_length

    def search_keyword_phrases(self,
                               text: str) -> List[str]:

        sentences = nltk.tokenize.sent_tokenize(text, language=self.__lang)

        cp = self._extract_contender_phrases(sentences)
        self._w_dist = Counter(chain.from_iterable(cp))
        self._deegree_rank = self._build_degree_rank(cp)
        return self._build_rank_list(cp)

    def _extract_contender_phrases(self, sentences: List[str]) -> MutableSet[Tuple[str, ...]]:
        contender_phrases = set()

        for sentence in sentences:
            sentence_word_tokens = [word.lower()
                                    for word in nltk.wordpunct_tokenize(sentence)]
            sentence_contender_phrases = self._generate_contender_phrases(
                sentence_word_tokens)
            contender_phrases.update(sentence_contender_phrases)

        return contender_phrases

    def _generate_contender_phrases(self, words: Generator[str, None, None]) -> Generator[Tuple[str, ...], None, None]:
        words_sequence = []

        for word in words:
            if word in ignorable_tokens:
                if self.__min_length <= len(words_sequence) <= self.__max_length:
                    yield tuple(words_sequence)
                words_sequence.clear()
                continue

            words_sequence.append(word)

    def _build_degree_rank(self, contender_phrases: MutableSet[Tuple[str, ...]]) -> Dict[str, int]:
        co_occurence_graph = defaultdict(lambda: defaultdict(lambda: 0))

        for cp in contender_phrases:
            for (word, coword) in product(cp, cp):
                co_occurence_graph[word][coword] += 1

        deegree_rank = defaultdict(lambda: 0)
        for key in co_occurence_graph:
            deegree_rank[key] = sum(co_occurence_graph[key].values())

        return deegree_rank

    def _build_rank_list(self, contender_phrases: MutableSet[Tuple[str, ...]]) -> List[str]:
        rank_list = []
        for phrase in contender_phrases:
            rank = sum(map(self._rank_phrase_word, phrase))
            rank_list.append((rank, " ".join(phrase)))

        rank_list.sort(reverse=True)
        return list(map(lambda t: t[1], rank_list))

    def _rank_phrase_word(self, word: str) -> float:
        return float(self._deegree_rank[word]) / self._w_dist[word]
