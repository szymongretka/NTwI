from core.granulation.granulizer import Granulizer
from core.keywords.keywords_searcher import search_keywords_in_granule
from core.granulation.granule import Granule


def granulize_text(text: str) -> Granule:
    granulizer = Granulizer()
    return granulizer.granulize(text)


def test_no_keywoards_for_empty_test():
    text = ""
    granule = granulize_text(text)
    keywords = search_keywords_in_granule(granule)

    assert len(keywords) == 0


def test_simple_sentence_for_keywoards_search():
    text = "The quick brown fox jumps over the lazy dog."
    granule = granulize_text(text)

    keywords = search_keywords_in_granule(granule)

    assert len(keywords) > 0
