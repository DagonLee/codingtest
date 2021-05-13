from collections import deque
w, h = map(int, input().split())
m = [list(input()) for _ in range(h)]
c = []
dx = [-1, 0, 0, 1]
dy = [0, -1, 1, 0]

for i in range(h):
	for j in range(w):
		if m[i][j] == 'C':
			c.append((i, j))

q = deque()

d = [[-1] * w for _ in range(h)]
q.append((c[0][0], c[0][1]))
d[c[0][0]][c[0][1]] = 0


while q:
	x, y = q.popleft()
	for k in range(4):
		nx, ny = x + dx[k], y + dy[k]
		while 0 <= nx < h and 0 <= ny < w:
			if m[nx][ny] == '*':
				break
			if d[nx][ny] == -1:
				d[nx][ny] = d[x][y] + 1
				q.append((nx, ny))
			nx, ny = nx + dx[k], ny + dy[k]


print(d[c[1][0]][c[1][1]] - 1)
