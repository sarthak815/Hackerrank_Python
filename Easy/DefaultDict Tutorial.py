from collections import defaultdict

n = list(map(int, input().split()))
n1 = n[0]
n2 = n[1]
if 0<n1<10001 and 0<n2<101:
	a = defaultdict(list)
	b = list()
	for i in range(n1):
		n3 = i + 1
		k = input()
		if 0<len(k)<100:
			a[k].append(n3)

	for j in range(n2):
		m = input()
		if 0<len(m)<101:
			b.append(m)


	for p in b:
		if p in a.keys():
			for i in a[p]:
				print(i, end = " ")
			print("")
		else:
			print("-1")

