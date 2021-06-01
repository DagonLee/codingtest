n, k = map(int, input().split())
lst = []
for _ in range(n):
	lst.append(int(input()))
d = [-1] * (k + 1)
d[0] = 0

for i in range(len(lst)):
	for j in range(k + 1):
		if j - lst[i] >= 0 and d[j - lst[i]] != -1:
			if d[j] == -1 or d[j] > d[j - lst[i]] + 1:
				d[j] = d[j - lst[i]] + 1
print(d[k])
