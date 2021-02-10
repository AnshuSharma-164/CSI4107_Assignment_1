import pandas as pd
import xlsxwriter
from nltk.corpus import stopwords
from nltk.tokenize import TweetTokenizer
import nltk
import re

stopwords = "StopWords.txt" #list stop words
tweets = "Trec_microblog11.txt" #txt of the original tweets


tknzr = TweetTokenizer()


stopWordsList = pd.read_csv(stopwords, sep="\n", header=None, error_bad_lines=False)
data = pd.read_csv(tweets, sep="\t", header=None, error_bad_lines=False)

stopWordsList.columns = ["words"]
data.columns = ["tweetID", "tweet"]
data.insert(2,"tokens", 1,allow_duplicates=True)
tweetList = data.loc[:,"tweet"]
stops = stopWordsList.loc[:,"words"]


tokenArray = []
tweetTokensCopy = []
for tweet in tweetList:
    tweetTokens = tknzr.tokenize(tweet)
    tweetTokensCopy = []
    for word in tweetTokens:
        word = word.lower()
        word = re.sub("\W+","a",word)
        word = re.sub("[0-9]+","a",word)
        if word not in stopWordsList.values:
            tweetTokensCopy.append(word)
    tokenArray.append(tweetTokensCopy)#TODO this does not recive updated list
# print(tokenArray)



# data.to_excel('output1.xlsx', engine='xlsxwriter')

