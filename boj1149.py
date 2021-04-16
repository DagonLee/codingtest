n = int(input())
d = [[0] * 3 for _ in range(n + 1)]
c = [[0] * 3 for _ in range(n + 1)]
for i in range(n):
	c[i + 1][0], c[i + 1][1], c[i + 1][2] = map(int, input().split())
for i in range(1, n + 1):
	d[i][0] = min(d[i - 1][1], d[i - 1][2]) + c[i][0]
	d[i][1] = min(d[i - 1][0], d[i - 1][2]) + c[i][1]
	d[i][2] = min(d[i - 1][0], d[i - 1][1]) + c[i][2]

print(min(d[n]))
