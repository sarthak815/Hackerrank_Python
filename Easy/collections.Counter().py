
from collections import Counter
n = int(input())
size = list(map(int,input().split()))
size = size[0:n+1]
n2 = int(input())
money = []
for i in range(n2):
    cost = list(map(int,input().split()))
    if size.count(cost[0])!= 0:
        money.append(cost[1])
        size.remove(cost[0])
print(sum(money))
