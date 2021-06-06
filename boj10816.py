from collections import defaultdict
d = defaultdict(int)
n = int(input())
a = list(map(int, input().split()))
for i in a:
	d[i] += 1
m = int(input())
b = list(map(int, input().split()))

for i in b:
	print(d[i], end=' ')
