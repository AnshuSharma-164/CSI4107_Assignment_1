import pandas as pd
import xlsxwriter
from nltk.corpus import stopwords
from nltk.tokenize import TweetTokenizer
import nltk
import re
import InvertedIndex

##########
# STEP 1 #
##########


stopwords = "StopWords.txt" #list stop words
tweets = "Trec_microblog11.txt" #txt of the original tweets

tknzr = TweetTokenizer()# create tokenizer

stopWordsList = pd.read_csv(stopwords, sep="\n", header=None, error_bad_lines=False) #stopwords dataset
data = pd.read_csv(tweets, sep="\t", header=None, error_bad_lines=False) #tweets dataset

stopWordsList.columns = ["words"]#set column name
data.columns = ["tweetID", "tweet"]#set column names
tweetList = data.loc[:,"tweet"]#create token array
tweetID = data.loc[:,"tweetID"]#create tweet ID
stops = stopWordsList.loc[:,"words"]#create stopword array

tweetList = tweetList[0:10]#TODO TEMPORARY TEST SET!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
tweetID = tweetID[0:10]#TODO TEMPORARY TEST SET!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

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
print(tokenArray)#for test purposes 


"""
add all tweetID and tweets to the Inverted Index
"""
corpusInvertedIndex = InvertedIndex.InvertedIndex()
for i in range(len(tweetID)):
    corpusInvertedIndex.insertTokenList(tokenArray[i],tweetID[i])


##########
# STEP 4 #
##########

# make queries
counter=0
queryList = []
queryFileAddress = "topics_MB1-49.txt"
queryFile = open(queryFileAddress, "r")
line = queryFile.readline()



#write the file
resultFile = open("Results.txt", "w")

#write the top 1000 results
"""
topic_id = the topic/query number (use the numbers, such a 1 instead of MB001)
Q0 = an unused field (the literal 'Q0')
docno = the tweet id, rank is the rank assigned by your system to the segment (1 is the highest rank)
score = the computed degree of match between the segment and the topic
tag = a unique identifier you chose for this run (same for every topic).
"""
topic_id, Q0, docno, rank, score, tag = 0, 0, 0, 0, 0, 0
resultFile.write("{}   {}   {}   {}   {}\n".format(topic_id, Q0, docno, rank, score, tag))



resultFile.close()