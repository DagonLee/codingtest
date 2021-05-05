n, m = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(n)]

for i in range(n):
	for j in range(m):
		if i != 0 and j != 0:
			matrix[i][j] += max(matrix[i - 1][j], matrix[i][j - 1])
		elif j != 0:
			matrix[i][j] += matrix[i][j - 1]
		elif i != 0:
			matrix[i][j] += matrix[i - 1][j]

print(matrix[n - 1][m - 1])
