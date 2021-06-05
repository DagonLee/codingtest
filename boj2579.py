n = int(input())
a = [0]
for _ in range(n):
	a.append(int(input()))

d = [[0] * 2 for _ in range(n + 1)]
d[1][0] = a[1]
d[1][1] = a[1]
for i in range(2, n + 1):
	d[i][0] = max(d[i - 2][0], d[i - 2][1]) + a[i]
	d[i][1] = d[i - 1][0] + a[i]

print(max(d[n]))
