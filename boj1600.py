from collections import deque
k = int(input())
w, h = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(h)]
d = [[[-1] * (k + 1) for i in range(w)] for j in range (h)]
hx = [-2, -2, -1, -1, 1, 1, 2, 2]
hy = [-1, 1, -2, 2, -2, 2, -1, 1]
dx = [-1, 0, 0, 1]
dy = [0, -1, 1, 0]
q = deque()
q.append((0, 0, 0))
d[0][0][0] = 0
while q:
	x, y, c = q.popleft()
	if c < k:
		for i in range(8):
			nx, ny = x + hx[i], y + hy[i]
			if nx < 0 or h <= nx or ny < 0 or w <= ny:
				continue
			if arr[nx][ny] == 0:
				if d[nx][ny][c + 1] == -1:
					d[nx][ny][c + 1] = d[x][y][c] + 1
					q.append((nx, ny, c + 1))
	for j in range(4):
		nx, ny = x + dx[j], y + dy[j]
		if nx < 0 or h <= nx or ny < 0 or w <= ny:
			continue
		if arr[nx][ny] == 0 and d[nx][ny][c] == -1:
			d[nx][ny][c] = d[x][y][c] + 1
			q.append((nx, ny, c))

ans = -1
for i in range(k + 1):
	if d[h - 1][w - 1][i] != -1:
		if ans == -1:
			ans = d[h - 1][w - 1][i]
		else:
			ans = min(ans, d[h - 1][w - 1][i])
print(ans)