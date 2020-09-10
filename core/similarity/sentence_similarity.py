
from core.granulation.granule import SentenceGranule
from math import log


def compute_similarity(lhs: SentenceGranule, rhs: SentenceGranule) -> float:
    common_words = set(lhs.lemmatized_non_stop_words) & set(
        rhs.lemmatized_non_stop_words)
    return len(common_words) / (log(len(lhs.lemmatized_non_stop_words)) + log(len(rhs.lemmatized_non_stop_words)))
