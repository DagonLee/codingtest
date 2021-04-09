n = int(input())
lst = list(map(int, input().split()))
d = [-1] * n
d[0] = 0
for i in range(1, n):
	for j in range(i):
		if d[j] != -1 and (i - j) <= lst[j]:
			if d[i] == -1 or d[i] > (d[j] + 1):
				d[i] = d[j] + 1
print(d[n - 1])
