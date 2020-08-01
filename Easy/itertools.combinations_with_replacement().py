from itertools import combinations_with_replacement
def convertTuple(tup): 
    str =  ''.join(tup) 
    return str
word, n = input().split()
word = sorted(word)
for i in list(combinations_with_replacement(word, int(n))):
	print(convertTuple(i))
