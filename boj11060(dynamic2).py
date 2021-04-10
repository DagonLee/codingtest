n = int(input())
lst = list(map(int, input().split()))
d = [-1] * n
d[0] = 0
for i in range(n - 1):
	if d[i] == -1:
		continue
	for j in range(1, lst[i] + 1):
		if i + j >= n:
			break
		elif d[i + j] == -1:
			d[i + j] = d[i] + 1

print(d[n - 1])