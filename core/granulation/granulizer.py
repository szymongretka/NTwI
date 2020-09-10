from core.granulation.granule import Granule, TextGranule, SentenceGranule, WordGranule
from nltk.tokenize import sent_tokenize
from nltk import pos_tag, wordpunct_tokenize
from core.tokenization.word_token import WordToken
from core.similarity.sentence_similarity import compute_similarity
from itertools import islice


class Granulizer(object):
    def granulize(self, text: str) -> Granule:
        sentences = sent_tokenize(text)
        sentences_granules = list(map(
            lambda s: self.create_sentence_granule(s), sentences))

        zipped = zip(islice(sentences_granules, len(
            sentences_granules) - 1), islice(sentences_granules, 1, None))
        print(list(map(lambda t: compute_similarity(t[0], t[1]), zipped)))

        return TextGranule(sentences_granules)

    def create_sentence_granule(self, sentence: str) -> SentenceGranule:
        words = wordpunct_tokenize(sentence)
        tagged_words = pos_tag(words)

        words_granules = map(lambda w: WordGranule(
            word_token=WordToken(word=w[0], pos_tag=w[1])), tagged_words)
        return SentenceGranule(words_granules)
