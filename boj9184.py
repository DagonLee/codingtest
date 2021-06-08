def go(a, b, c):
	if a <= 0 or b <= 0 or c <= 0:
		return 1
	if a > 20 or b > 20 or c > 20:
		return go(20, 20, 20)
	if d[a][b][c] != -1:
		return d[a][b][c]
	elif a < b < c:
		d[a][b][c] = go(a, b, c - 1) + go(a, b - 1, c - 1) - go(a, b - 1, c)
	else:
		d[a][b][c] = go(a - 1, b, c) + go(a - 1, b - 1, c) + go(a - 1, b, c - 1) - go(a - 1, b - 1, c - 1)
	return d[a][b][c]


d = [[[-1] * 21 for i in range(21)] for j in range(21)]
while True:
	i, j, k = map(int, input().split())
	if i == -1 and j == -1 and k == -1:
		break
	print('w({}, {}, {}) = {}'.format(i, j, k, go(i, j, k)))
