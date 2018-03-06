import csv, re, sys
import string
import collections
from regex import *
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.corpus import stopwords
import itertools
import unicodedata



def read_tweets():
    '''
        Read all tweets from a combined csv file
        Return a list of tweets
    '''

    all_tweets = []
    try:
        with open ('./data/tweets_data/combined.csv') as f:
            rows = csv.reader(f)
            for row in rows:
                all_tweets.append(row[2])
    except:
        sys.exit(1)

    return all_tweets

def tweets_cleaning(all_tweets):
    '''
        Read the tweets from the read_tweets() function and prepare
        preprocessing procedures.

        Remove the stopwords, english sentence, links and emoticons

        retrun a plain tweets
    '''

    # remove stop words
    stop_words = set(stopwords.words('arabic1'))

    # remove the emoticons
    emoji_pattern = re.compile("["
            u"\U0001F600-\U0001F64F"  # emoticons
            u"\U0001F300-\U0001F5FF"  # symbols & pictographs
            u"\U0001F680-\U0001F6FF"  # transport & map symbols
            u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
                               "]+", flags=re.UNICODE)

    # where to stop the cleaned tweets
    cleand_tweets = []

    for row in all_tweets:
        data = re.sub(r"http\S+", " ", row).strip()
        data = re.sub("[a-zA-Z\d+\W+\_@#:.///]", " ", data).strip()
        tweets = emoji_pattern.sub(r'',data).strip()
        sentence = re.sub(r"\s+", " ", tweets, flags=re.UNICODE).strip()
        cleand_tweets.append(sentence)
        for word in word_tokenize(sentence):
            print(word)
            ### TO DO ##
            ### Toeknizing the words and get the sentiments ###



    # Building a simple lexicons
    lexicons = []
    for tweet in cleand_tweets:
         for word in word_tokenize(tweet):
                  words = ''.join(ch for ch, _ in itertools.groupby(word))
                  if words not in stop_words:
                       lexicons.append(words)


def main():
    tweets = read_tweets()
    tweets_cleaning(tweets)


if __name__ == '__main__':
    main()
