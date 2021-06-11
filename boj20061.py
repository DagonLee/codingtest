a = [[0] * 10 for _ in range(10)]
n = int(input())
ans = 0


def border_arrange():
	r = 0
	c = 0
	for i in range(2):
		if a[0][4 + i] == 1 or a[1][4 + i] == 1 or a[2][4 + i] == 1 or a[3][4 + i] == 1:
			c += 1
		if a[4 + i][0] == 1 or a[4 + i][1] == 1 or a[4 + i][2] == 1 or a[4 + i][3] == 1:
			r += 1
	for _ in range(r):
		row_arrange(9)
	for _ in range(c):
		col_arrange(9)


def row_arrange(idx):
	for i in range(idx, 4, -1):
		for j in range(4):
			a[i][j] = a[i - 1][j]
	a[4][0] = a[4][1] = a[4][2] = a[4][3] = 0
	return


def col_arrange(idx):
	for j in range(idx, 4, -1):
		for i in range(4):
			a[i][j] = a[i][j - 1]
	a[0][4] = a[1][4] = a[2][4] = a[3][4] = 0
	return


def full_arrange():
	global ans
	check = False
	for i in range(9, 3, -1):
		if a[i][0] + a[i][1] + a[i][2] + a[i][3] == 4:
			ans += 1
			check = True
			row_arrange(i)
		if a[0][i] + a[1][i] + a[2][i] + a[3][i] == 4:
			ans += 1
			check = True
			col_arrange(i)
	return check


for _ in range(n):
	t, x, y = map(int, input().split())
	if t == 1:
		for i in range(x, 10):
			if a[i][y] == 1:
				a[i - 1][y] = 1
				break
			if i == 9:
				a[9][y] = 1
		for j in range(y, 10):
			if a[x][j] == 1:
				a[x][j - 1] = 1
				break
			if j == 9:
				a[x][9] = 1
	if t == 2:
		for i in range(x, 10):
			if a[i][y] == 1 or a[i][y + 1] == 1:
				a[i - 1][y] = a[i - 1][y + 1] = 1
				break
			if i == 9:
				a[9][y] = a[9][y + 1] = 1
		for j in range(y + 1, 10):
			if a[x][j] == 1:
				a[x][j - 1] = a[x][j - 2] = 1
				break
			if j == 9:
				a[x][9] = a[x][8] = 1
	if t == 3:
		for i in range(x + 1, 10):
			if a[i][y] == 1:
				a[i - 1][y] = a[i - 2][y] = 1
				break
			if i == 9:
				a[9][y] = a[8][y] = 1
		for j in range(y, 10):
			if a[x][j] == 1 or a[x + 1][j] == 1:
				a[x][j - 1] = a[x + 1][j - 1] = 1
				break
			if j == 9:
				a[x][9] = a[x + 1][9] = 1
	while full_arrange():
		pass
	border_arrange()
block = 0
for i in range(4):
	for j in range(4):
		if a[i][j + 6] == 1:
			block += 1
		if a[i + 6][j] == 1:
			block += 1
print(ans)
print(block)

