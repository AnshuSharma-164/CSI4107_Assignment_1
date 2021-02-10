import math
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
		#UGLY CODE THAT RUINS MY DAY!
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
		return str(self.index)

	"""
	Insert token to the inverted index.
	"""
	def insertToken(self, token, tweetId):
		self.idList.add(tweetId)
		self.N = len(self.idList)
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


	def idf(self, token):
		if token in index.keys():
			return math.log(self.N/len(self.index[token]), 2)
		else:
			return 0

	###########################################
	#Finish Tomorrow                          #
	###########################################
	def normalizeTf(self, token, tweetId):
		maxTf = 0
		for tf in self.index[token].values():
			if tf>maxTf:
				maxTf = tf
		return self.index[token][tweetId]/maxTf


	def documentWeight(self, token, tweetId):
		return self.normalizeTf(token, tweetId)*self.idf(token)

	def queryWeight(self, token):
		return 2#do

	def maxTf(self);
		return 2#do

	def cosineSim(self, Query):
		return 2#do

