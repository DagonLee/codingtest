dx = [0, -1, 0, 1]
dy = [1, 0, -1, 0]

r, c, t = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(r)]
robot_x = 0
ans = 0
for i in range(r):
	for j in range(c):
		if matrix[i][j] == -1:
			robot_x = i


def pollute(x, y, arr):
	p_lst = []
	for i in range(4):
		nx, ny = x + dx[i], y + dy[i]
		if nx < 0 or r <= nx or ny < 0 or c <= ny or matrix[nx][ny] == -1:
			continue
		p_lst.append((nx, ny))
	arr[x][y] -= (matrix[x][y] // 5) * len(p_lst)
	for i, j in p_lst:
		arr[i][j] += (matrix[x][y] // 5)


def clean(x, y, s):
	prev = 0
	s_x = x
	s_y = y + 1
	d = 0
	while s_x != x or s_y != y:
		tmp = matrix[s_x][s_y]
		matrix[s_x][s_y] = prev
		prev = tmp
		s_x, s_y = s_x + dx[d], s_y + dy[d]
		if s_x < 0 or r <= s_x or s_y < 0 or c <= s_y:
			s_x, s_y = s_x - dx[d], s_y - dy[d]
			if s == 0:
				d = (d + 1) % 4
			elif s == 1:
				d = (d + 3) % 4
			s_x, s_y = s_x + dx[d], s_y + dy[d]


while t:
	spread = [[0] * c for _ in range(r)]
	for i in range(r):
		for j in range(c):
			if matrix[i][j] >= 5:
				pollute(i, j, spread)
	for i in range(r):
		for j in range(c):
			matrix[i][j] += spread[i][j]
	clean(robot_x - 1, 0, 0)
	clean(robot_x, 0, 1)
	t -= 1
for i in range(r):
	for j in range(c):
		if matrix[i][j] != -1:
			ans += matrix[i][j]

print(ans)
