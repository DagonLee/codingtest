n, k = map(int, input().split())
lst = []
for _ in range(n):
	lst.append(int(input()))

d = [0] * (k + 1)
d[0] = 1

for i in range(len(lst)):
	for j in range(1, k + 1):
		if j - lst[i] >= 0:
			d[j] += d[j - lst[i]]

print(d[k])