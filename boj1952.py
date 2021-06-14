dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
m, n = map(int, input().split())
d = [[-1] * n for _ in range(m)]
k = 0
x, y = 0, 0
d[x][y] = 0
ans = 0
i = 1
while i < m * n:
	nx, ny = x + dx[k], y + dy[k]
	if nx < 0 or m <= nx or ny < 0 or n <= ny or d[nx][ny] != -1:
		ans += 1
		k = (k + 1) % 4
		nx, ny = x + dx[k], y + dy[k]
	x, y = nx, ny
	d[nx][ny] = i
	i += 1

print(ans)