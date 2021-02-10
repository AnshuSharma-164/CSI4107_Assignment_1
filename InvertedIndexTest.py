import InvertedIndex

print("Test 1 \n")

test = InvertedIndex.InvertedIndex()

test.insertToken("new" , "d1")
test.insertToken("york", "d1")
test.insertToken("times" , "d1")
test.insertToken("new" , "d2")
test.insertToken("york", "d2")
test.insertToken("post" , "d2")
test.insertTokenList(["los", "angeles", "times"] , "d3")
print(test)

print("idf scores \n")

x = []
x.append(test.idf("angeles"))
x.append(test.idf("los"))
x.append(test.idf("new"))
x.append(test.idf("post"))
x.append(test.idf("times"))
x.append(test.idf("york"))
print(x)

print("\n document tf idf\n")

y = []
y_1 = []
y_1.append( test.normalizeTf("angeles" , "d1") )
y_1.append( test.normalizeTf("los" , "d1") )
y_1.append( test.normalizeTf("new" , "d1") )
y_1.append( test.normalizeTf("post" , "d1") )
y_1.append( test.normalizeTf("times" , "d1") )
y_1.append( test.normalizeTf("york" , "d1") )
y.append(y_1)
y_2 = []
y_2.append( test.normalizeTf("angeles" , "d2") )
y_2.append( test.normalizeTf("los" , "d2") )
y_2.append( test.normalizeTf("new" , "d2") )
y_2.append( test.normalizeTf("post" , "d2") )
y_2.append( test.normalizeTf("times" , "d2") )
y_2.append( test.normalizeTf("york" , "d2") )
y.append(y_2)
y_3 = []
y_3.append( test.normalizeTf("angeles" , "d3") )
y_3.append( test.normalizeTf("los" , "d3") )
y_3.append( test.normalizeTf("new" , "d3") )
y_3.append( test.normalizeTf("post" , "d3") )
y_3.append( test.normalizeTf("times" , "d3") )
y_3.append( test.normalizeTf("york" , "d3") )
y.append(y_3)
for l in y: print(l)

print("\n")

z = []
z_1 = []
z_1.append( test.documentWeight("angeles" , "d1") )
z_1.append( test.documentWeight("los" , "d1") )
z_1.append( test.documentWeight("new" , "d1") )
z_1.append( test.documentWeight("post" , "d1") )
z_1.append( test.documentWeight("times" , "d1") )
z_1.append( test.documentWeight("york" , "d1") )
z.append(z_1)
z_2 = []
z_2.append( test.documentWeight("angeles" , "d2") )
z_2.append( test.documentWeight("los" , "d2") )
z_2.append( test.documentWeight("new" , "d2") )
z_2.append( test.documentWeight("post" , "d2") )
z_2.append( test.documentWeight("times" , "d2") )
z_2.append( test.documentWeight("york" , "d2") )
z.append(z_2)
z_3 = []
z_3.append( test.documentWeight("angeles" , "d3") )
z_3.append( test.documentWeight("los" , "d3") )
z_3.append( test.documentWeight("new" , "d3") )
z_3.append( test.documentWeight("post" , "d3") )
z_3.append( test.documentWeight("times" , "d3") )
z_3.append( test.documentWeight("york" , "d3") )
z.append(z_3)
for l in z: print(l)

print("\n query tf idf \n")

q = []
q.append( test.queryWeight("angeles", ["new", "new", "times"]) )
q.append( test.queryWeight("los", ["new", "new", "times"]) )
q.append( test.queryWeight("new", ["new", "new", "times"]) )
q.append( test.queryWeight("post", ["new", "new", "times"]) )
q.append( test.queryWeight("times", ["new", "new", "times"]) )
q.append( test.queryWeight("york", ["new", "new", "times"]) )
print(q)

print("COSINESIM TEST START\n")

#cos_sim = np.dot(doc_vector,query_vector)/(np.linalg.norm(doc_vector)*np.linalg.norm(query_vector))

c = test.cosineSim(["new", "new", "times"], "d1")

print(c)

print("COSINESIM TEST END \n")


print("\n test 2 \n")

test_2 = InvertedIndex.InvertedIndex()

test_2.insertTokenList(["new", "new", "times"] , "d")

a = test_2.normalizeTf("new" , "d")
b = test_2.normalizeTf("times" , "d")

print([a,b])
