from core.granulation.granule import Granule, TextGranule, SentenceGranule, WordGranule
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk import pos_tag
from core.tokenization.word_token import WordToken


class Granulizer(object):
    def granulize(self, text: str) -> Granule:
        sentences = sent_tokenize(text)
        sentences_granules = map(
            lambda s: self.create_sentence_granule(s), sentences)
        return TextGranule(list(sentences_granules))

    def create_sentence_granule(self, sentence: str) -> SentenceGranule:
        words = word_tokenize(sentence)
        tagged_words = pos_tag(words)

        words_granules = map(lambda w: WordGranule(
            word_token=WordToken(word=w[0], pos_tag=w[1])), tagged_words)
        return SentenceGranule(words_granules)
