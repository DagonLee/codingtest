n = int(input())
lst = []
for _ in range(n):
	lst.append(list(map(int, input().split())))
lst.sort()
for i in lst:
	print(i[0], i[1])
