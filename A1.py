import pandas as pd
import xlsxwriter
from nltk.corpus import stopwords
from nltk.tokenize import TweetTokenizer
import nltk

stopwords = "StopWords.txt" #list stop words
tweets = "Trec_microblog11.txt" #txt of the original tweets


tknzr = TweetTokenizer()


stopWordsList = pd.read_csv(stopwords, sep="\n", header=None, error_bad_lines=False)
data = pd.read_csv(tweets, sep="\t", header=None, error_bad_lines=False)

data.columns = ["tweetID", "tweet"]
data.insert(2,"tokens", 1,allow_duplicates=True)
x = data.loc[:,"tweet"]

tokenArray = []
# counter=0#TODO this is for if you add it to the data structre
for tweet in x:
    # if counter>1:#TODO this is for if you add it to the data structre
    #     break
    tweetTokens = tknzr.tokenize(tweet)
    tokenArray.append(tweetTokens)
    # # data.replace({counter: tweetTokens})#TODO this is for if you add it to the data structre
    # data.at[counter,'tokens'] = tweetTokens
    # counter+=1
print(tokenArray)
    
#tokens_without_sw = [word for word in text_tokens if not word in stopwords.words()]


# data.to_excel('output1.xlsx', engine='xlsxwriter')
