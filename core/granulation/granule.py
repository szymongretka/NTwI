from typing import List, Generator
from abc import ABC, abstractmethod
from core.tokenization.word_token import WordToken


class Granule(ABC):
    @abstractmethod
    def to_string(self) -> str:
        pass

    @abstractmethod
    def get_word_tokens_iter(self) -> Generator[WordToken, None, None]:
        pass


class WordGranule(Granule):
    def __init__(self, word_token: WordToken):
        self.word_token = word_token

    def get_word_tokens_iter(self) -> Generator[WordToken, None, None]:
        yield self.word_token

    def to_string(self) -> str:
        return self.word_token.word


class SentenceGranule(Granule):
    def __init__(self, words_granules: List[WordGranule]):
        self.words_granules = words_granules

    def get_word_tokens_iter(self) -> Generator[WordToken, None, None]:
        for word in self.words_granules:
            yield word.word_token

    def to_string(self) -> str:
        return ''.join([' {0} '.format(granule.to_string()) for granule in self.words_granules])


class TextGranule(Granule):
    def __init__(self, sentences_granules: List[SentenceGranule]):
        self.sentences_granules = sentences_granules

    def get_word_tokens_iter(self) -> Generator[WordToken, None, None]:
        sentences = len(self.sentences_granules)
        for sentence in self.sentences_granules:
            for word in sentence.words_granules:
                yield word.word_token

    def to_string(self) -> str:
        return ''.join([granule.to_string() for granule in self.sentences_granules])
