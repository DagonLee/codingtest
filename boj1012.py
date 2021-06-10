t = int(input())
dx = [-1, 0, 0, 1]
dy = [0, -1, 1, 0]


def dfs(x, y):
	for k in range(4):
		nx, ny = x + dx[k], y + dy[k]
		if nx < 0 or n <= nx or ny < 0 or m <= ny:
			continue
		if a[nx][ny] == 1 and not check[nx][ny]:
			check[nx][ny] = True
			dfs(nx, ny)


for _ in range(t):
	m, n, g = map(int, input().split())
	a = [[0] * m for _ in range(n)]
	check = [[False] * m for _ in range(n)]
	for i in range(g):
		y, x = map(int, input().split())
		a[x][y] = 1
	cnt = 0
	for i in range(n):
		for j in range(m):
			if a[i][j] == 1 and not check[i][j]:
				cnt += 1
				check[i][j] = True
				dfs(i, j)
	print(cnt)
