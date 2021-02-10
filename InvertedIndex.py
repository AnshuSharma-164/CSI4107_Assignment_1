import numpy as np
"""
The file contains the inverted index class. The inverted index
structure is used through this assignment for easier indexing and 
Retrieval and Ranking.
Author: Anshu Sharma
"""
class InvertedIndex:

	"""
	This is the constructor for the inverted index class.
	"""
	def __init__ (self):
		self.index = {}
		self.idList = set()
		self.N = len(self.idList)

	"""
	TODO: comment
	"""
	def __repr__ (self):
		text = self.showIndex()
		return text

	"""
	TODO: comment
	"""
	def __str__ (self):
		text = self.showIndex()
		return text

	"""
	TODO: to be re-implimented to show the first few values of the index
	and not the entire index.
	"""
	def showIndex(self):
		text = ""
		for token in self.index:
			text = text+token+ " : "+str(self.index[token])+"\n"
		return text

	"""
	Insert token to the inverted index.
	"""
	def insertToken(self, token, tweetId):
		self.idList.add(tweetId) #update set of tweetId's 
		self.N = len(self.idList) #update the size of the set of tweetId's
		if token in self.index:
			if tweetId in self.index[token]:
				self.index[token][tweetId] += 1
			else:
				self.index[token][tweetId] = 1
		else:
			self.index[token] = { tweetId:1 }

	"""
	Insert an list of token with same tweet Id
	into the inverted index.
	"""
	def insertTokenList(self, tokenList, tweetId):
		for token in tokenList:
			self.insertToken(token, tweetId)

	"""
	Helper function for the weighting functions.
	This function takes in a token and find's the 
	token idf in the inverted index.
	"""
	def idf(self, token):
		if token in self.index: #If token is in the inverted index the the function does the idf calculation.
			return np.log2(self.N/len(self.index[token]))
		else: #returns 0 otherwise.
			return 0.0


	def normalizeTf(self, token, tweetId):
		if tweetId in self.index[token]:
			maxTf = 0
			for key in self.index:
				if tweetId in self.index[key] and maxTf < self.index[key][tweetId]:
					maxTf = self.index[key][tweetId]
			return self.index[token][tweetId]/maxTf
		else:
			return 0.0


	def queryTf(self, token, query):
		return query.count(token)/query.count(max(set(query), key = query.count))


	def documentWeight(self, token, tweetId):
		return self.normalizeTf(token, tweetId)*self.idf(token)


	def queryWeight(self, token, query):
		return (0.5+0.5*self.queryTf(token, query))*self.idf(token)


	def cosineSim(self, query):
		return 2#do

	def rankedRetrieval(self, query):
		return 2#do
