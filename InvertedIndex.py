class InvertedIndex:

	def __init__ (self, index=[]):
		self.index = index


	def __repr__ (self):
		text = self.showIndex()
		return text


	def __str__ (self):
		text = self.showIndex()
		return text


	def showIndex(self):
		text = ""
		for wordPair in self.index:
			text = text+wordPair[0]
			for idPair in wordPair[1]:
				text = text + " " + str(idPair[0])+":"+str(idPair[1])
			text = text+"\n"
		return text


	def insertToken(self, token, tweetId):
		tokenInIndex = False
		for item in self.index:
			if(token==item[0]):
				self.addId(item[1], tweetId)
				tokenInIndex = True
		if(tokenInIndex==False):
			self.index.append( (token, [ (tweetId, 1) ]) )

	def insertTokenList(self, tokenList, tweetId):
		for token in tokenList:
			self.insertToken(token, tweetId)


	def addId(self, IdList, tweetId):
		IdInList = False
		for pair in IdList:
			if ( tweetId == pair[0] ):
				pair[1] = pair[1]+1
				IdInList = True
		if(IdInList==False):
			IdList.append((tweetId,1))

