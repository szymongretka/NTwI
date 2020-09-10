from typing import List
from core.tokenization.word_token import WordToken
import string
import nltk
import re
from itertools import chain

__punctuations = string.punctuation
__stopwords = nltk.corpus.stopwords.words('english')
ignorable_tokens = set(chain(__stopwords, __punctuations))


def filter_stop_word_tokens(tokens: List[WordToken]) -> List[WordToken]:
    return list(filter(_filter_meaningless_pos_tags, filter(lambda t: t.word.lower() not in ignorable_tokens, tokens)))


def _filter_meaningless_pos_tags(token: WordToken) -> bool:
    return token.pos_tag not in {'CD', 'LS', 'POS', 'UH'}
