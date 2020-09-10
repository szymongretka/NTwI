
from core.granulation.granule import SentenceGranule
from math import log10


def compute_similarity(lhs: SentenceGranule, rhs: SentenceGranule) -> float:
    common_words = set(lhs.lemmatized_non_stop_words) & set(
        rhs.lemmatized_non_stop_words)
    numerator = len(common_words)

    lhs_len = len(lhs.lemmatized_non_stop_words)
    rhs_len = len(rhs.lemmatized_non_stop_words)
    denominator = log10(lhs_len) + \
        log10(rhs_len) if lhs_len > 0 and rhs_len > 0 else 0

    return numerator / denominator if denominator != 0 else 0
