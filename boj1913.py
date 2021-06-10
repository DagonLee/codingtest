n = int(input())
a = int(input())
d = [[0] * n for _ in range(n)]
x, y = 0, 0
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
r = 0
num = n * n
d[x][y] = num
while True:
	nx, ny = x + dx[r], y + dy[r]
	if nx < 0 or n <= nx or ny < 0 or n <= ny or d[nx][ny] != 0:
		r = (r + 1) % 4
		nx, ny = x + dx[r], y + dy[r]
	if num != 1:
		num -= 1
		d[nx][ny] = num
		x, y = nx, ny
	else:
		break
ans = ''
for i in range(n):
	for j in range(n):
		print(d[i][j], end=' ')
		if d[i][j] == a:
			ans += str(i + 1) + ' ' + str(j + 1)
	print()
print(ans)