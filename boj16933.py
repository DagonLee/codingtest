from collections import deque
n, m, k = map(int, input().split())
matrix = [list(map(int, list(input()))) for _ in range(n)]
d = [[[[0] * 2 for i in range(11)] for j in range(1000)] for a in range(1000)]

q = deque()
q.append((0, 0, 0, 0))
dx = [-1, 0, 0, 1]
dy = [0, -1, 1, 0]
d[0][0][0][0] = 1

while q:
	x, y, c, w = q.popleft()
	for i in range(4):
		nx, ny = x + dx[i], y + dy[i]
		if nx < 0 or n <= nx or ny < 0 or m <= ny:
			continue
		if matrix[nx][ny] == 0 and d[nx][ny][c][1 - w] == 0:
			d[nx][ny][c][1 - w] = d[x][y][c][w] + 1
			q.append((nx, ny, c, 1 - w))
		if w == 0 and c + 1 <= k and matrix[nx][ny] == 1 and d[nx][ny][c + 1][1 - w] == 0:
			d[nx][ny][c + 1][1 - w] = d[x][y][c][w] + 1
			q.append((nx, ny, c + 1, 1 - w))
	if d[x][y][c][1 - w] == 0:
		d[x][y][c][1 - w] = d[x][y][c][w] + 1
		q.append((x, y, c, 1 - w))

ans = -1
for i in range(2):
	for j in range(k + 1):
		if d[n - 1][m - 1][j][i] == 0:
			continue
		if ans == -1:
			ans = d[n - 1][m - 1][j][i]
		elif ans > d[n - 1][m - 1][j][i]:
			ans = d[n - 1][m - 1][j][i]


print(ans)

