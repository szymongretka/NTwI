from core.granulation.granulizer import Granulizer


class TextSumarizer(object):
    def __init__(self, granulizer: Granulizer):
        super().__init__()
        self.__granulizer = granulizer

    def summarize(self, text: str) -> str:
        granule = self.__granulizer.granulize(text)
        return granule.to_string()
