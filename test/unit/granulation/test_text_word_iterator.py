from core.granulation.granule import TextGranule, SentenceGranule, WordGranule, WordToken


def test_text_word_token_iterator_empty():
    text = TextGranule(sentences_granules=[])
    iterator = text.get_word_tokens_iter()
    assert len(list(iterator)) == 0


def test_text_word_token_iterator_with_sentences():
    sentences = [
        SentenceGranule([
            WordGranule(WordToken("NN", "NLP")),
            WordGranule(WordToken("VBZ", "is")),
            WordGranule(WordToken("NN", "fun")),
        ], 'NLP is fun'),
        SentenceGranule([
            WordGranule(WordToken("NN", "So")),
            WordGranule(WordToken("VBZ", "is")),
            WordGranule(WordToken("NN", "python")),
        ], 'So is python'),
        SentenceGranule([], ''),
    ]
    text = TextGranule(sentences)
    iterator = text.get_word_tokens_iter()
    assert len(list(iterator)) == 6
