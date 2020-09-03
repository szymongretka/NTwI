from core.text_summarizer import TextSumarizer
from core.granulation.granulizer import Granulizer

if __name__ == "__main__":
    import sys
    text = sys.stdin.read()
    granulizer = Granulizer()
    summarizer = TextSumarizer(granulizer)
    summarized_text = summarizer.summarize(text)
    print(summarized_text, end='')

# porter = PorterStemmer()
# lancaster = LancasterStemmer()

# file = open("test.txt")
# my_lines_list = file.readlines()

# def stemSentence(sentence):
#     token_words = word_tokenize(sentence)
#     token_words
#     stem_sentence = []
#     for word in token_words:
#         stem_sentence.append(porter.stem(word))
#         stem_sentence.append(" ")
#     return "".join(stem_sentence)

# print(my_lines_list[0])
# print("Stemmed sentence")
# x = stemSentence(my_lines_list[0])
# print(x)

# stem_file = open("result.txt", mode="a+", encoding="utf-8")
# for line in my_lines_list:
#     stem_sentence = stemSentence(line)
#     stem_file.write(stem_sentence)


# text_file = nltk.corpus.gutenberg.words('melville-moby_dick.txt')
# my_lines_list2 = []
# for line in text_file:
#     my_lines_list2.append(line)
# my_lines_list2

# stem_file.close()
