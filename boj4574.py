cnt = 0
dx = [0, 1]
dy = [1, 0]
while True:
	n = int(input())
	if n == 0:
		break
	board = [[0] * 9 for _ in range(9)]
	row_check = [[False] * 10 for _ in range(9)]
	col_check = [[False] * 10 for _ in range(9)]
	part_check = [[False] * 10 for _ in range(9)]
	domino = [[False] * 10 for _ in range(10)]
	for _ in range(n):
		s = input().split()
		x1 = ord(s[1][0]) - ord('A')
		y1 = int(s[1][1]) - 1
		x2 = ord(s[3][0]) - ord('A')
		y2 = int(s[3][1]) - 1
		board[x1][y1] = int(s[0])
		row_check[x1][int(s[0])] = True
		col_check[y1][int(s[0])] = True
		part_check[(x1 // 3) * 3 + y1 // 3][int(s[0])] = True
		board[x2][y2] = int(s[2])
		row_check[x2][int(s[2])] = True
		col_check[y2][int(s[2])] = True
		part_check[(x2 // 3) * 3 + y2 // 3][int(s[2])] = True
		domino[int(s[0])][int(s[2])] = domino[int(s[2])][int(s[0])] = True
	nums = input().split()
	for i in range(len(nums)):
		x = ord(nums[i][0]) - ord('A')
		y = int(nums[i][1]) - 1
		board[x][y] = i + 1
		row_check[x][i + 1] = True
		col_check[y][i + 1] = True
		part_check[(x // 3) * 3 + y // 3][i + 1] = True


	def go(z):
		if z == 81:
			for i in board:
				print(''.join(map(str, i)))
			return True
		x = z // 9
		y = z % 9
		if board[x][y] != 0:
			return go(z + 1)
		else:
			for k in range(2):
				nx, ny = x + dx[k], y + dy[k]
				if nx < 0 or 9 <= nx or ny < 0 or 9 <= ny:
					continue
				if board[nx][ny] != 0:
					continue
				for i in range(1, 10):
					for j in range(1, 10):
						if i == j:
							continue
						if domino[i][j]:
							continue
						if not col_check[y][i] and not row_check[x][i] and not part_check[(x // 3) * 3 + y // 3][i]:
							if not col_check[ny][j] and not row_check[nx][j] and not part_check[(nx // 3) * 3 + ny // 3][j]:
								row_check[x][i] = True
								col_check[y][i] = True
								part_check[(x // 3) * 3 + y // 3][i] = True
								board[x][y] = i
								row_check[nx][j] = True
								col_check[ny][j] = True
								part_check[(nx // 3) * 3 + ny // 3][j] = True
								board[nx][ny] = j
								domino[i][j] = domino[j][i] = True
								if go(z + 1):
									return True
								row_check[x][i] = False
								col_check[y][i] = False
								part_check[(x // 3) * 3 + y // 3][i] = False
								board[x][y] = 0
								row_check[nx][j] = False
								col_check[ny][j] = False
								part_check[(nx // 3) * 3 + ny // 3][j] = False
								domino[i][j] = domino[j][i] = False
								board[nx][ny] = 0
		return False
	cnt += 1
	print('Puzzle' + ' ' + str(cnt))
	go(0)
