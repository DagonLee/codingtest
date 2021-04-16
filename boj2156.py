n = int(input())
a = [0] * (n + 1)
for i in range(n):
	a[i + 1] = int(input())
d = [[0] * 3 for _ in range(n + 1)]
for i in range(1, n + 1):
	d[i][2] = d[i - 1][1] + a[i]
	d[i][1] = a[i] + d[i - 1][0]
	d[i][0] = max(d[i - 1][0], d[i - 1][1], d[i - 1][2])
print(max(d[n]))
