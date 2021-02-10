import pandas as pd
import xlsxwriter
from nltk.corpus import stopwords
from nltk.tokenize import TweetTokenizer
import nltk
import re

stopwords = "StopWords.txt" #list stop words
tweets = "Trec_microblog11.txt" #txt of the original tweets

tknzr = TweetTokenizer()# create tokenizer

stopWordsList = pd.read_csv(stopwords, sep="\n", header=None, error_bad_lines=False) #stopwords dataset
data = pd.read_csv(tweets, sep="\t", header=None, error_bad_lines=False) #tweets dataset

stopWordsList.columns = ["words"]#set column name
data.columns = ["tweetID", "tweet"]#set column names
data.insert(2,"tokens", 1,allow_duplicates=True)#create token row
tweetList = data.loc[:,"tweet"]#create token array
stops = stopWordsList.loc[:,"words"]#create stopword array


tokenArray = []
tweetTokensCopy = []
for tweet in tweetList:
    tweetTokens = tknzr.tokenize(tweet) # tokenize tweets
    tweetTokensCopy = []
    for word in tweetTokens:
        word = word.lower() #set all tweet tokens lowercase
        word = re.sub("\W+","a",word) #remove non-alphabet characters
        word = re.sub("[0-9]+","a",word) #remove numbers
        if word not in stopWordsList.values: # only add to output non-stopwords
            tweetTokensCopy.append(word)
    tokenArray.append(tweetTokensCopy) #add tweet tokens to output
# print(tokenArray)



# data.to_excel('output1.xlsx', engine='xlsxwriter')

