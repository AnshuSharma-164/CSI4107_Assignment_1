import InvertedIndex

test = InvertedIndex.InvertedIndex()

test.insertToken("new" , "d1")
test.insertToken("york", "d1")
test.insertToken("times" , "d1")
test.insertToken("new" , "d2")
test.insertToken("york", "d2")
test.insertToken("post" , "d2")
test.insertTokenList(["los", "angeles", "times"] , "d3")
print(test)

x = []
x.append(test.idf("angeles"))
x.append(test.idf("los"))
x.append(test.idf("new"))
x.append(test.idf("post"))
x.append(test.idf("times"))
x.append(test.idf("york"))
print(x)

y = test.normalizeTf("times" , "d1")
#print(y)

z = test.documentWeight("times", "d1")
#print(z)

q = test.queryWeight("times", ["new", "new", "times"])
print(q)
