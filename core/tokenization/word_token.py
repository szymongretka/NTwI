class WordToken(object):
    def __init__(self, pos_tag: str, word: str):
        self.pos_tag = pos_tag
        self.word = word

    def __repr__(self) -> str:
        return repr(dict(tag=self.pos_tag, word=self.word))
