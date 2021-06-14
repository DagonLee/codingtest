n = int(input())
m = int(input())
d = [[0] * n for _ in range(n)]
x, y = (n - 1) // 2, (n - 1) // 2
d[x][y] = 1
num = 2
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
for i in range(3, n + 1, 2):
	x, y = x + dx[3], y + dy[3]
	d[x][y] = num
	num += 1
	for k in range(4):
		size = i - 1
		if k == 0:
			size -= 1
		for j in range(size):
			x, y = x + dx[k], y + dy[k]
			d[x][y] = num
			num += 1
ax, ay = 0, 0
for i in range(n):
	for j in range(n):
		if d[i][j] == m:
			ax, ay = i + 1, j + 1
		print(d[i][j], end=' ')
	print()
print(ax, ay)