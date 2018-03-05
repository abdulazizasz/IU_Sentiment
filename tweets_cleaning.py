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


def getWordLists():
    '''
    Retrieve the stop words, negation words, exempt words, positive emojies
    and negative emojies from files and save them in lists

    return a bunch of list
    '''
    stopWords = [line[0] for line in csv.reader(open('stop_words.txt','r'))]
    negationWords = [line[0] for line in csv.reader(open('negation_words.txt','r'))]
    exemptWords = [line[0] for line in csv.reader(open('exempt_words.txt', 'r'))]
    posEmojis = [line[0] for line in csv.reader(open('pos_emojis.txt', 'r'))]
    negEmojis = [line[0] for line in csv.reader(open('neg_emojis.txt','r'))]

    return stopWords, negationWords, exemptWords, posEmojis, negEmojis



def main():
    all_tweets = []
    try:
        with open ('./data/combined.csv') as f:
            rows = csv.reader(f)
            for row in rows:
                all_tweets.append(row[2])
    except:
        sys.exit(1)


    # stopwords
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


    lexicons = []
    for tweet in cleand_tweets:
         for word in word_tokenize(tweet):
                  words = ''.join(ch for ch, _ in itertools.groupby(word))
                  if words not in stop_words:
                       lexicons.append(words)

    print(len(lexicons))





if __name__ == '__main__':
    main()
