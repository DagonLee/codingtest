from collections import deque
n, m = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(n)]
dx = [0, 0, -1, 1, 1, 1, -1, -1]
dy = [1, -1, 0, 0, 1, -1, -1, 1]


def bfs(r, c):
	q = deque()
	q.append((r, c))
	dist = [[-1] * m for _ in range(n)]
	dist[r][c] = 0
	while q:
		x, y = q.popleft()
		for i in range(8):
			nx, ny = x + dx[i], y + dy[i]
			if nx < 0 or n <= nx or ny < 0 or m <= ny:
				continue
			if matrix[nx][ny] == 1:
				return dist[x][y] + 1
			if dist[nx][ny] == -1:
				dist[nx][ny] = dist[x][y] + 1
				q.append((nx, ny))


ans = -1
for i in range(n):
	for j in range(m):
		if matrix[i][j] == 0:
			tmp = bfs(i, j)
			ans = max(ans, tmp)

print(ans)