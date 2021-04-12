def check(x1, y1, x2, y2):
	out1 = False
	out2 = False
	if x1 < 0 or n <= x1 or y1 < 0 or m <= y1:
		out1 = True
	if x2 < 0 or n <= x2 or y2 < 0 or m <= y2:
		out2 = True
	if out1 and out2:
		return -1
	elif out1 or out2:
		return 1


def move(x1, y1, x2, y2, i):
	nx1, ny1, nx2, ny2 = x1, y1, x2, y2
	if i == 0: # 좌
		if (y1 > 0 and board[x1][y1 - 1] != '#') or y1 == 0:
			ny1 = y1 -1
		if (y2 > 0 and board[x2][y2 - 1] != '#') or y2 == 0:
			ny2 = y2 - 1
	elif i == 1: #우
		if (y1 < m - 1 and board[x1][y1 + 1] != '#') or y1 == m - 1:
			ny1 = y1 + 1
		if (y2 < m - 1 and board[x2][y2 + 1] != '#') or y2 == m - 1:
			ny2 = y2 + 1
	elif i == 2: # 위
		if (x1 > 0 and board[x1 - 1][y1] != '#') or x1 == 0:
			nx1 = x1 - 1
		if (x2 > 0 and board[x2 - 1][y2] != '#') or x2 == 0:
			nx2 = x2 - 1
	elif i == 3:  # 아래
		if (x1 < n - 1 and board[x1 + 1][y1] != '#') or x1 == n - 1:
			nx1 = x1 + 1
		if (x2 < n - 1 and board[x2 + 1][y2] != '#') or x2 == n - 1:
			nx2 = x2 + 1
	return nx1, ny1, nx2, ny2


def go(cnt, x1, y1, x2, y2):
	if cnt == 11:
		return
	res = check(x1, y1, x2, y2)
	if res == -1:
		return
	elif res == 1:
		global ans
		ans = min(ans, cnt)
		return
	for i in range(4):
		new = move(x1, y1, x2, y2, i)
		nx1, ny1, nx2, ny2 = new[0], new[1], new[2], new[3]
		go(cnt + 1, nx1, ny1, nx2, ny2)


n, m = map(int, input().split())
board = [list(input()) for _ in range(n)]
ans = 11
b_lst = []
for i in range(n):
	for j in range(m):
		if board[i][j] == 'o':
			b_lst.append((i, j))
			board[i][j] = '.'
go(0, b_lst[0][0], b_lst[0][1], b_lst[1][0], b_lst[1][1])

if ans == 11:
	print(-1)
else:
	print(ans)