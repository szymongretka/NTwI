from core.keywords.keywords_searcher import RAKEKeywordsSearcher


def test_no_keywoards_for_empty_test():
    text = ""
    searcher = RAKEKeywordsSearcher()
    keywords_phrases = searcher.search_keyword_phrases(text)

    assert len(keywords_phrases) == 0


def test_simple_sentence_for_keywoards_search():
    # (PDF) Automatic Keyword Extraction from Individual Documents. Available from: https://www.researchgate.net/publication/227988510_Automatic_Keyword_Extraction_from_Individual_Documents.

    text = """
    Compatibility of systems of linear constraints over the set of natural numbers.
    
    Criteria of compatibility of a system of linear Diophantine equations, strict inequations, and nonstrict inequations are considered. 
    Upper bounds for components of a minimal set of solutions and algorithms of construction of minimal generating sets of solutions for all types of systems are given. 
    These criteria and the corresponding algorithms for constructing a minimal supporting set of solutions can be used in solving all the considered types of systems and systems of mixed types. 
    """

    searcher = RAKEKeywordsSearcher()
    top_keywords_phrases = searcher.search_keyword_phrases(text)[:10]

    assert 'linear diophantine equations' in top_keywords_phrases
    assert 'minimal supporting set' in top_keywords_phrases
    assert 'natural numbers' in top_keywords_phrases
