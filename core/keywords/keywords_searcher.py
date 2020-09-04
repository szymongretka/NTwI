from typing import List
from core.granulation.granule import Granule
from core.tokenization.word_token import WordToken
from nltk.corpus import stopwords

__stopwords = set(map(lambda w: w.lower(), stopwords.words('english')))
__all_pos_tags = ["CC", "CD", "DT", "EX", "FW", "IN", "JJ", "JJR", "JJS", "LS", "MD", "NN", "NNS", "NNP", "NNPS", "PDT", "POS",
                  "PRP", "PRP$", "RB", "RBR", "RBS", "RP", "SYM", "TO", "UH", "VB", "VBD", "VBG", "VBN", "VBP", "VBZ", "WDT", "WP", "WP$", "WRB"]
__meaningful_pos_tags = set(
    ["FW", "JJ", "NN", "NNS", "VB", "VBD", "VBN", "VBZ"])


def search_keywords_in_granule(granule: Granule) -> List[str]:
    iterator = granule.get_word_tokens_iter()

    tokens_without_stop_words = filter(lambda token: token.word.lower()
                                       not in __stopwords, iterator)
    tokens_with_meaningful_pos = filter(
        __filter_based_on_pos, tokens_without_stop_words)

    return list(map(lambda t: t.word, tokens_with_meaningful_pos))


def __filter_based_on_pos(token: WordToken) -> bool:
    return token.pos_tag in __meaningful_pos_tags
