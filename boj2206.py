from collections import deque
q = deque()
n, m = map(int, input().split())
dx = [-1, 0, 0, 1]
dy = [0, -1, 1, 0]
d = [[[0] * 2 for j in range(m)] for i in range(n)]
matrix = []
for _ in range(n):
	matrix.append(list(map(int, list(input()))))
q.append((0, 0, 0))
d[0][0][0] = 1
while q:
	x, y, z = q.popleft()
	for k in range(4):
		nx, ny = x + dx[k], y + dy[k]
		if 0 <= nx < n and 0 <= ny < m:
			if matrix[nx][ny] == 0 and d[nx][ny][z] == 0:
				d[nx][ny][z] = d[x][y][z] + 1
				q.append((nx, ny, z))
			if z == 0 and matrix[nx][ny] == 1 and d[nx][ny][z + 1] == 0:
				d[nx][ny][z + 1] = d[x][y][z] + 1
				q.append((nx, ny, z + 1))

if d[n - 1][m - 1][0] != 0 and d[n - 1][m - 1][1] != 0:
	print(min(d[n - 1][m - 1]))
elif d[n - 1][m - 1][0] != 0:
	print(d[n - 1][m - 1][0])
elif d[n - 1][m - 1][1] != 0:
	print(d[n - 1][m - 1][1])
else:
	print(-1)
