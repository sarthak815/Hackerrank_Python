k = set()
for i in range(int(input())):
	word = input()
	if word not in k:
		k.add(word)
print(len(k))