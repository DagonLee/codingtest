n, m = map(int, input().split())
d = [[0] * n for _ in range(n)]
for _ in range(m):
	i, j = map(int, input().split())
	d[i - 1][j - 1] += 1
	d[j - 1][i - 1] += 1
ans = -1
for i in range(n - 2):
	for j in range(i + 1, n - 1):
		if d[i][j] != 0:
			for k in range(j + 1, n):
				if d[i][k] != 0 and d[j][k] != 0:
					if ans == -1 or ans > sum(d[i]) + sum(d[j]) + sum(d[k]) - 6:
						ans = sum(d[i]) + sum(d[j]) + sum(d[k]) - 6

print(ans)