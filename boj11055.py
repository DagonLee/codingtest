n = int(input())
a = [0] + list(map(int, input().split()))
d = [0] * (n + 1)
for i in range(1, n + 1):
	d[i] = a[i]
	for j in range(1, i):
		if a[i] > a[j] and d[j] + a[i] > d[i]:
			d[i] = d[j] + a[i]
print(max(d))
