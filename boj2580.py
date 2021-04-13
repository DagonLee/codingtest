board = [list(map(int, input().split())) for _ in range(9)]
row_check = [[False] * 10 for _ in range(9)]
col_check = [[False] * 10 for _ in range(9)]
part_check = [[False] * 10 for _ in range(9)]


def dfs(z):
	if z == 81:
		for i in range(9):
			for j in range(9):
				print(board[i][j], end=' ')
			print()
		return True
	x = z // 9
	y = z % 9
	if board[x][y] != 0:
		return dfs(z + 1)
	else:
		for i in range(1, 10):
			if not row_check[x][i] and not col_check[y][i] and not part_check[(x // 3) * 3 + y // 3][i]:
				row_check[x][i] = True
				col_check[y][i] = True
				part_check[(x // 3) * 3 + y // 3][i] = True
				board[x][y] = i
				if dfs(z + 1):
					return True
				board[x][y] = 0
				row_check[x][i] = False
				col_check[y][i] = False
				part_check[(x // 3) * 3 + y // 3][i] = False
	return False


for i in range(9):
	for j in range(9):
		if board[i][j] != 0:
			row_check[i][board[i][j]] = True
			col_check[j][board[i][j]] = True
			part_check[(i // 3) * 3 + j // 3][board[i][j]] = True
dfs(0)