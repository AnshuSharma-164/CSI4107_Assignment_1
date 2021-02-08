import pandas as pd
import xlsxwriter

tweets = "Trec_microblog11.txt"

data = pd.read_csv(tweets, sep="\t", header=None, error_bad_lines=False)
data.columns = ["a", "b"]
# data.to_excel("tweets.xlsx")
data.to_excel('output1.xlsx', engine='xlsxwriter')  
