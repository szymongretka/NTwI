from core.text_summarizer import TextSumarizer
from core.granulation.granulizer import Granulizer

if __name__ == "__main__":
    import sys
    text = sys.stdin.read()
    granulizer = Granulizer()
    summarizer = TextSumarizer(granulizer)
    summarized_text = summarizer.summarize(text)
    print(summarized_text, end='')
