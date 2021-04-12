n, m = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(n)]
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]
ans = 0
visit = [[False] * m for _ in range(n)]


def go(cnt, s, visit, x, y):
	if cnt == 4:
		global ans
		ans = max(ans, s)
		return
	for i in range(4):
		nx, ny = x + dx[i], y + dy[i]
		if nx < 0 or n <= nx or ny < 0 or m <= ny:
			continue
		if not visit[nx][ny]:
			visit[nx][ny] = True
			go(cnt + 1, s + matrix[nx][ny], visit, nx, ny)
			visit[nx][ny] = False


for i in range(n):
	for j in range(m):
		visit[i][j] = True
		go(1, matrix[i][j], visit, i, j)
		visit[i][j] = False
		if i <= (n - 2) and j <= (m - 3):
			ans = max(ans, matrix[i][j] + matrix[i][j + 1] + matrix[i][j + 2] + matrix[i + 1][j + 1])
			ans = max(ans, matrix[i + 1][j] + matrix[i][j + 1] + matrix[i + 1][j + 1] + matrix[i + 1][j + 2])
		if i <= (n - 3) and j <= (m - 2):
			ans = max(ans, matrix[i][j] + matrix[i + 1][j] + matrix[i + 2][j] + matrix[i + 1][j + 1])
			ans = max(ans, matrix[i][j + 1] + matrix[i + 1][j] + matrix[i + 1][j + 1] + matrix[i + 2][j + 1])
print(ans)