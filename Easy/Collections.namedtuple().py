from collections import namedtuple
n , school = int(input()),  namedtuple("school", input().split())
marks = [int(school(*input().split()).MARKS) for i in range(n)]
print(sum(marks)/n)
