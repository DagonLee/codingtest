from collections import deque

n, m, k = map(int, input().split())
matrix = [list(map(int, list(input()))) for _ in range(n)]

d = [[[-1] * (k + 1) for i in range(m)] for j in range(n)]
dx = [-1, 0, 0, 1]
dy = [0, -1, 1, 0]

q = deque()
q.append((0, 0, 0))
d[0][0][0] = 1
while q:
	x, y, c = q.popleft()
	for i in range(4):
		nx, ny = x + dx[i], y + dy[i]
		if nx < 0 or n <= nx or ny < 0 or m <= ny:
			continue
		if matrix[nx][ny] == 0 and d[nx][ny][c] == -1:
			d[nx][ny][c] = d[x][y][c] + 1
			q.append((nx, ny, c))
		if matrix[nx][ny] == 1 and c < k and d[nx][ny][c + 1] == -1:
			d[nx][ny][c + 1] = d[x][y][c] + 1
			q.append((nx, ny, c + 1))

ans = 1000001
for i in range(k + 1):
	if d[n - 1][m - 1][i] != -1:
		ans = min(ans, d[n - 1][m - 1][i])
print(ans if ans != 1000001 else -1)