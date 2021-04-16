n, m = map(int, input().split())
board = [list(input()) for _ in range(n)]
visit = [[False] * m for _ in range(n)]
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]


def dfs(x, y, px, py, color):
	if visit[x][y]:
		return True
	visit[x][y] = True
	for k in range(4):
		nx, ny = x + dx[k], y + dy[k]
		if nx < 0 or n <= nx or ny < 0 or m <= ny:
			continue
		if px == nx and py == ny:
			continue
		if board[nx][ny] == color:
			if dfs(nx, ny, x, y, color):
				return True
	return False


for i in range(n):
	for j in range(m):
		if not visit[i][j]:
			if dfs(i, j, -1, -1, board[i][j]):
				print('Yes')
				exit()
print('No')