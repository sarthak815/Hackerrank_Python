from itertools import combinations
word, n = input().split()
for i in range(1, int(n)+1):
    lst1 = list(combinations(sorted(str(word)), i))
    for j in lst1:
        print(''.join(map(str,j)))