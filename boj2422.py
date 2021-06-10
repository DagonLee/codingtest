n, m = map(int, input().split())
d = [[False] * n for _ in range(n)]
for _ in range(m):
	i, j = map(int, input().split())
	d[i - 1][j - 1] = d[j - 1][i - 1] = True
cnt = 0
for i in range(n - 2):
	for j in range(i + 1, n - 1):
		for k in range(j + 1, n):
			if d[i][j] or d[j][k] or d[k][i]:
				continue
			cnt += 1
print(cnt)