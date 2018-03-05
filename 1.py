import csv, re, sys
import string
import collections
from regex import *
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.corpus import stopwords
import itertools
import unicodedata
from nltk.tag.stanford import StanfordPOSTagger
from nltk.tag.stanford import CoreNLPPOSTagger
from nltk.tokenize.stanford import CoreNLPTokenizer

all_tweets = []

with open ('./data/combined.csv') as f:
    rows = csv.reader(f)
    for row in rows:
        all_tweets.append(row[2])


stop_words = set(stopwords.words('arabic1'))

# remove the emoticons
emoji_pattern = re.compile("["
        u"\U0001F600-\U0001F64F"  # emoticons
        u"\U0001F300-\U0001F5FF"  # symbols & pictographs
        u"\U0001F680-\U0001F6FF"  # transport & map symbols
        u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
                           "]+", flags=re.UNICODE)

cleand_tweets = []

for row in all_tweets:
    data = re.sub(r"http\S+", " ", row)
    data = re.sub("[a-zA-Z\d+\W+\_@#:.///]", " ", data)
    tweets = emoji_pattern.sub(r'',data).strip()
    sentence = re.sub(r"\s+", " ", tweets, flags=re.UNICODE)
    cleand_tweets.append(sentence)
    for word in word_tokenize(sentence):
        if word not in stop_words:
            print(word)
