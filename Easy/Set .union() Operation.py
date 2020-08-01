n1 = int(input())
nos1 = list(map(int, input().split()))
nos1 = nos1[:n1]
nos1 = set(nos1)
n2 = int(input())
nos2 = list(map(int, input().split()))
nos2 = nos2[:n2]
nos2 = set(nos2)
nos1 = nos1.union(nos2)
print(len(nos1))

