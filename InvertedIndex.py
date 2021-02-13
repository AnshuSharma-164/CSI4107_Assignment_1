
import numpy as np
"""
The file contains the inverted index class. The inverted index
structure is used through this assignment for easier indexing and 
Retrieval and Ranking.
Author: Anshu Sharma
"""
##########
# STEP 2 #
##########
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
		if token in self.index: #if token token is in index already updates the token's value dictionary
			if tweetId in self.index[token]:
				self.index[token][tweetId] += 1
			else:
				self.index[token][tweetId] = 1
		else: #else add token to the index.
			self.index[token] = { tweetId:1 }

	"""
	Insert an list of token with same tweet Id
	into the inverted index.
	"""
	def insertTokenList(self, tokenList, tweetId):
		for token in tokenList: #loops throught the list of token calling the insertToken function.
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

	"""
	Helper function to normalize document term frequency.
	This function takes in a token and tweetId then normalize
	the token's term frequency to tweet that's connected to the 
	tweetId.
	"""
	def normalizeTf(self, token, tweetId):
		if tweetId in self.index[token]:#checks if word was written in the tweet connected to tweetId.
			#maxTf = 0 #finds frequency of the most common term from the tweet connected to tweetId.
			#for key in self.index: #checks every word in the index to find the most common in the document.
			#	if tweetId in self.index[key] and maxTf < self.index[key][tweetId]:
			#		maxTf = self.index[key][tweetId]
			return self.index[token][tweetId]
		else:
			return 0.0

	"""
	Helper function for the queryWeight function.
	takes in a token and the query then calculates
	the token's normalized term frequency in the query.
	"""
	def queryTf(self, token, query):
		if token in query:
			return query.count(token)/query.count(max(set(query), key = query.count)) #term frequency of token in query / term frequency for the most frequent term in query
		else:
			return 0.0

	"""
	Function to obtain the weight of a token for a given
	document in the inverted index. This function takes
	attribute token and tweetId and calls two helper functions
	to comput the tf-idf.
	"""
	def documentWeight(self, token, tweetId):
		return self.normalizeTf(token, tweetId)*self.idf(token) #calls helper function define above and multiply together.

	"""
	Function to obtain weight of a token in a given query.
	The function calls two helper function to calculate the
	tf_q-idf which is used for the weighting.
	"""
	def queryWeight(self, token, query):
		if token in self.index and token in query:
			return self.queryTf(token, query)*self.idf(token) #calls helper function define above and multiply together.
		else:
			return 0

	##########
	# STEP 3 #
	##########

	def cosineSim(self, query, tweetId, tweetnorm):

		dot_product = 0
		query_norm = 0
		for token in query:
			query_frequency = 0
			doc_frequency = 0
			query_frequency  = self.queryTf(token, query)
			if token in self.index:
				doc_frequency = self.normalizeTf(token, tweetId)
			idf = self.idf(token)
			dot_product = dot_product + (query_frequency*doc_frequency*idf*idf)
			query_norm = query_norm + (query_frequency*idf)**2
		query_norm = np.sqrt(query_norm)
		document_norm = np.sqrt(tweetnorm[tweetId])


		#cosine similarity formula using py
		cos_sim = 0
		if document_norm!=0:
			cos_sim = dot_product/(query_norm*document_norm)
		return cos_sim
		#return [doc_vector, query_vector]

	def rankedRetrieval(self, query):

		data = {}
		query_normsqr = 0
		for token in self.index:

			idf = np.log2(self.N/len(self.index[token]))

			tf_q = 0
			if token in query:
				tf_q = query.count(token)
				query_normsqr += (tf_q*idf)**2 


			for tweetId in self.index[token]:
				tf_d  = self.index[token][tweetId]
				if tweetId in data:
					data[tweetId][0] += tf_d*tf_q*(idf**2)
					data[tweetId][1] += (tf_d*idf)**2
				else:
					data[tweetId] = [tf_d*tf_q*(idf**2) , (tf_d*idf)**2]

		query_norm = np.sqrt(query_normsqr)
		rankedResults = []
		for i in data:
			document_norm = np.sqrt(data[i][1])
			if query_norm!=0:
				cos_sim = data[i][0]/(query_norm*document_norm)
			else:
				cos_sim = 0
			rankedResults.append((i, cos_sim))
		#loop through every tweetId in idList and find cosine similarity
		#for tweetId in self.idList:
		#	rankedResults.append((tweetId, self.cosineSim(query, tweetId, document_normsqr)))
		
		#Sort HERE
		rankedResults.sort(key=lambda x: x[1])

		rankedResults.reverse()

		return rankedResults
		
