def go(cnt, x1, y1, x2, y2):
	if cnt == 11:
		return -1
	out1 = False
	out2 = False
	if x1 < 0 or n <= x1 or y1 < 0 or m <= y1:
		out1 = True
	if x2 < 0 or n <= x2 or y2 < 0 or m <= y2:
		out2 = True
	if out1 and out2:
		return -1
	elif out1 or out2:
		return cnt
	ans = -1
	for i in range(4):
		nx1, ny1, nx2, ny2 = x1 + dx[i], y1 + dy[i], x2 + dx[i], y2 + dy[i]
		if 0 <= nx1 < n and 0 <= ny1 < m and board[nx1][ny1] == '#':
			nx1, ny1 = x1, y1
		if 0 <= nx2 < n and 0 <= ny2 < m and board[nx2][ny2] == '#':
			nx2, ny2 = x2, y2
		tmp = go(cnt + 1, nx1, ny1, nx2, ny2)
		if tmp == -1:
			continue
		if ans == -1 or ans > tmp:
			ans = tmp
	return ans


n, m = map(int, input().split())
board = [list(input()) for _ in range(n)]
b_lst = []
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]
for i in range(n):
	for j in range(m):
		if board[i][j] == 'o':
			b_lst.append((i, j))
			board[i][j] = '.'
print(go(0, b_lst[0][0], b_lst[0][1], b_lst[1][0], b_lst[1][1]))
