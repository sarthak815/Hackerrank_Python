from collections import OrderedDict
od = {}
for i in range(int(input())):
	item, quantity= input().rsplit(' ', 1)
	if od.get(item):
		od[item] = od.get(item, 0) + int(quantity)
	else:
		od[item] = int(quantity)
for k, v in od.items():
    print(k, v)