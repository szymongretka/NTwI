# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import nltk
from nltk.stem import PorterStemmer
from nltk.stem import LancasterStemmer
from nltk.tokenize import sent_tokenize, word_tokenize

# nltk.download()

porter = PorterStemmer()
lancaster = LancasterStemmer()

file=open("test.txt")
my_lines_list=file.readlines()
my_lines_list

def stemSentence(sentence):
    token_words=word_tokenize(sentence)
    token_words
    stem_sentence=[]
    for word in token_words:
        stem_sentence.append(porter.stem(word))
        stem_sentence.append(" ")
    return "".join(stem_sentence)

print(my_lines_list[0])
print("Stemmed sentence")
x=stemSentence(my_lines_list[0])
print(x)

stem_file=open("result.txt",mode="a+", encoding="utf-8")
for line in my_lines_list:
    stem_sentence=stemSentence(line)
    stem_file.write(stem_sentence)


text_file=nltk.corpus.gutenberg.words('melville-moby_dick.txt')
my_lines_list2=[]
for line in text_file:
    my_lines_list2.append(line)
my_lines_list2

stem_file.close()