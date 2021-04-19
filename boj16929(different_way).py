n, m = map(int, input().split())
board = [list(input()) for _ in range(n)]
visit = [[False] * m for _ in range(n)]
d = [[0] * m for _ in range(n)]
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]


def dfs(i, j, cnt, color):
	if visit[i][j]:
		return cnt - d[i][j] >= 4
	visit[i][j] = True
	d[i][j] = cnt
	for k in range(4):
		nx, ny = i + dx[k], j + dy[k]
		if nx < 0 or n <= nx or ny < 0 or m <= ny:
			continue
		if color == board[nx][ny]:
			if dfs(nx, ny, cnt + 1, color):
				return True
	return False


for i in range(n):
	for j in range(m):
		if not visit[i][j]:
			if dfs(i, j, 0, board[i][j]):
				print('Yes')
				exit()
print('No')
