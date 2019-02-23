#from nltk.stem import PorterStemmer

import nltk
import matplotlib.pyplot as plt
#nltk.download()
from nltk.probability import FreqDist
from nltk.stem import PorterStemmer
from nltk.stem import LancasterStemmer
import nltk
from nltk.stem import WordNetLemmatizer


porter = PorterStemmer()
lancaster = LancasterStemmer()
lancaster = LancasterStemmer()

path = "/Users/charankottapalli/Documents/GitHub/CS5542_BigdataApplications/Lab 1/Token/questions.txt"
file =open(path, "r")
sentence = file.read()


wordnet_lemmatizer = WordNetLemmatizer()

punctuations = "?:!.,;"
sentence_words = nltk.word_tokenize(sentence)
for word in sentence_words:
    if word in punctuations:
        sentence_words.remove(word)


print(sentence_words)
file = open("file.txt", "w")
print("{0:20}{1:20}".format("Word", "Lemma"))
for word in sentence_words:
    print("{0:20}{1:20}".format(word, wordnet_lemmatizer.lemmatize(word, pos="v")))
    file.write(wordnet_lemmatizer.lemmatize(word, pos="v")+" ")

file = open("file.txt", "r")
text = file.read()

file.close()

file = open("file.txt", "r+")
wordcount = {}
for word in file.read().split():
    if word not in wordcount:
        wordcount[word] = 1
    else:
        wordcount[word] += 1
print(word, wordcount)
file.close()



