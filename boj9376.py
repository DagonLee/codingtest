from collections import deque
t = int(input())
dx = [-1, 0, 0, 1]
dy = [0, -1, 1, 0]


def bfs(m, i, j):
	r = len(m)
	a = len(m[0])
	d = [[-1] * a for _ in range(r)]
	q = deque()
	q.append((i, j))
	d[i][j] = 0
	while q:
		x, y = q.popleft()
		for k in range(4):
			nx, ny = x + dx[k], y + dy[k]
			if 0 <= nx < r and 0 <= ny < a and d[nx][ny] == -1 and m[nx][ny] != '*':
				if m[nx][ny] == '#':
					d[nx][ny] = d[x][y] + 1
					q.append((nx, ny))
				else:
					d[nx][ny] = d[x][y]
					q.appendleft((nx, ny))
	return d


while t:
	h, w = map(int, input().split())
	m = ['.' + input() + '.' for _ in range(h)]
	h += 2
	w += 2
	m = ['.' * w] + m + ['.' * w]
	c = []
	ans = 10000
	d0 = bfs(m, 0, 0)
	for i in range(h):
		for j in range(w):
			if m[i][j] == '$':
				c.append((i, j))
	d1 = bfs(m, c[0][0], c[0][1])
	d2 = bfs(m, c[1][0], c[1][1])
	for i in range(h):
		for j in range(w):
			if d0[i][j] == -1 or d1[i][j] == -1 or d2[i][j] == -1:
				continue
			if m[i][j] == '*':
				continue
			cur = d0[i][j] + d1[i][j] + d2[i][j]
			if m[i][j] == '#':
				cur -= 2
			ans = min(ans, cur)
	print(ans)
	t -= 1
