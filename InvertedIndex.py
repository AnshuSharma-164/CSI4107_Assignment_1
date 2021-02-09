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



