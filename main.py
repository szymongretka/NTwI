from core.text_summarizer import TextSumarizer
from core.granulation.granulizer import Granulizer

if __name__ == "__main__":
    import sys
    ratio = float(sys.argv[1]) if len(sys.argv) >= 2 else 0.1

    text = sys.stdin.read()
    granulizer = Granulizer()
    summarizer = TextSumarizer(granulizer)
    summarized_text = summarizer.summarize(text, ratio=ratio)
    print(summarized_text, end='')
