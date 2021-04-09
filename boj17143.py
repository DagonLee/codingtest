dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]
r, c, m = map(int, input().split())
matrix = [[[] for _ in range(c)] for _ in range(r)]
for _ in range(m):
	i, j, s, d, z = map(int, input().split())
	matrix[i - 1][j - 1].append([s, z, d - 1])
ans = 0
t = 0


def move(matrix):
	tmp = [[[] for _ in range(c)] for _ in range(r)]
	for i in range(r):
		for j in range(c):
			if matrix[i][j]:
				sp, si, di = matrix[i][j][0]
				matrix[i][j].pop()
				nx, ny = i + dx[di] * sp, j + dy[di] * sp
				while nx < 0 or r <= nx or ny < 0 or c <= ny:
					if nx < 0:
						nx = abs(nx)
						di = 1
					elif r <= nx:
						nx = (2 * r) - nx - 2
						di = 0
					elif ny < 0:
						ny = abs(ny)
						di = 2
					elif c <= ny:
						ny = (2 * c) - ny - 2
						di = 3
				tmp[nx][ny].append([sp, si, di])

	return tmp


while t < c:
	for i in range(r):
		if matrix[i][t]:
			ans += matrix[i][t][0][1]
			matrix[i][t].pop()
			break
	tmp_matrix = move(matrix)

	for i in range(r):
		for j in range(c):
			if tmp_matrix[i][j]:
				tmp_matrix[i][j].sort(key=lambda x: x[1], reverse=True)
				matrix[i][j].append(tmp_matrix[i][j][0])

	t += 1
print(ans)
