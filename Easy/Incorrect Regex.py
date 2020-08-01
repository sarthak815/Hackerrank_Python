import re
for i in range(int(input())):
	ans = "True"
	try:
		re.compile(str(input()))
	except re.error as e:
		ans = "False"
	print(ans)