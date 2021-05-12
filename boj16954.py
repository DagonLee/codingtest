from collections import deque
matrix = [list(input()) for _ in range(8)]
q = deque()
dx = [-1, 0, 0, 1, 1, 1, -1, -1, 0]
dy = [0, -1, 1, 0, 1, -1, 1, -1, 0]
d = [[[0] * 9 for i in range(8)] for j in range(8)]
q.append((7, 0, 0))


while q:
	x, y, t = q.popleft()
	for i in range(9):
		nx, ny = x + dx[i], y + dy[i]
		nt = min(t + 1, 8)
		if nx < 0 or 8 <= nx or ny < 0 or 8 <= ny:
			continue
		if nx - t >= 0 and matrix[nx - t][ny] != '.':
			continue
		if nx - t - 1 >= 0 and matrix[nx - t - 1][ny] != '.':
			continue
		if d[nx][ny][nt] == 0:
			d[nx][ny][nt] = d[x][y][t] + 1
			q.append((nx, ny, nt))

for i in d[0][7]:
	if i != 0:
		print(1)
		exit()
print(0)
