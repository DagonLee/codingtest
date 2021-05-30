n, s, m = map(int, input().split())
v = list(map(int, input().split()))
d = [[0] * (m + 1) for _ in range(n + 1)]
d[0][s] = 1

for i in range(n):
	for j in range(m + 1):
		if d[i][j] == 1:
			if j - v[i] >= 0:
				d[i + 1][j - v[i]] = 1
			if j + v[i] <= m:
				d[i + 1][j + v[i]] = 1

for i in range(m, -1, -1):
	if d[n][i] == 1:
		print(i)
		exit()
print(-1)
