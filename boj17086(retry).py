from collections import deque
n, m = map(int ,input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
dx = [-1, 0, 0, 1, -1, 1, -1, 1]
dy = [0, -1, 1, 0, -1, 1, 1, -1]


def bfs(i, j):
	q = deque()
	q.append((i, j))
	d = [[-1] * m for _ in range(n)]
	d[i][j] = 0
	while q:
		x, y = q.popleft()
		for k in range(8):
			nx, ny = x + dx[k], y + dy[k]
			if nx < 0 or n <= nx or ny < 0 or m <= ny:
				continue
			if d[nx][ny] == -1:
				if arr[nx][ny] == 1:
					return d[x][y] + 1
				else:
					d[nx][ny] = d[x][y] + 1
					q.append((nx, ny))


ans = -1
for i in range(n):
	for j in range(m):
		if arr[i][j] == 0:
			ans = max(ans, bfs(arr, i, j))
print(ans)