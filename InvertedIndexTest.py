import InvertedIndex

test = InvertedIndex.InvertedIndex()
test.insertToken("new" , 1)
test.insertToken("york", 1)
test.insertToken("times" , 1)
test.insertToken("new" , 2)
test.insertToken("york", 2)
test.insertToken("post" , 2)
test.insertTokenList(["los", "angeles", "times"] , 3)
print(test)