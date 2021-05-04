from collections import deque

n, m = map(int, input().split())
matrix = []
ans = 0
dx = [-1, 0, 0, 1]
dy = [0, 1, -1, 0]
for _ in range(n):
	matrix.append(list(map(int, input().split())))


def count(matrix):
	q = deque()
	cnt = 0
	tmp_matrix = [[0] * m for _ in range(n)]
	for i in range(n):
		for j in range(m):
			tmp_matrix[i][j] = matrix[i][j]
			if matrix[i][j] == 2:
				q.append((i, j))
	while q:
		x, y = q.popleft()
		for k in range(4):
			nx, ny = x + dx[k], y + dy[k]
			if 0 <= nx < n and 0 <= ny < m:
				if tmp_matrix[nx][ny] == 0:
					tmp_matrix[nx][ny] = 2
					q.append((nx, ny))
	for i in range(n):
		for j in range(m):
			if tmp_matrix[i][j] == 0:
				cnt += 1
	return cnt


for x1 in range(n):
	for y1 in range(m):
		if matrix[x1][y1] != 0:
			continue
		for x2 in range(n):
			for y2 in range(m):
				if matrix[x2][y2] != 0:
					continue
				for x3 in range(n):
					for y3 in range(m):
						if matrix[x3][y3] != 0:
							continue
						if x1 == x2 and y1 == y2:
							continue
						if x1 == x3 and y1 == y3:
							continue
						if x2 == x3 and y2 == y3:
							continue
						matrix[x1][y1] = 1
						matrix[x2][y2] = 1
						matrix[x3][y3] = 1
						cur = count(matrix)
						if ans < cur:
							ans = cur
						matrix[x1][y1] = 0
						matrix[x2][y2] = 0
						matrix[x3][y3] = 0
print(ans)
