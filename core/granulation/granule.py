from typing import List
from abc import ABC, abstractmethod
from core.tokenization.word_token import WordToken


class Granule(ABC):
    @abstractmethod
    def to_string(self) -> str:
        pass


class WordGranule(Granule):
    def __init__(self, word_token: WordToken):
        self.word_token = word_token

    def to_string(self) -> str:
        return self.word_token.word


class SentenceGranule(Granule):
    def __init__(self, words_granules: List[WordGranule]):
        self.words_granules = words_granules

    def to_string(self) -> str:
        return ''.join([' {0} '.format(granule.to_string()) for granule in self.words_granules])


class TextGranule(Granule):
    def __init__(self, sentences_granules: List[SentenceGranule]):
        self.sentences_granules = sentences_granules

    def to_string(self) -> str:
        return ''.join([granule.to_string() for granule in self.sentences_granules])
