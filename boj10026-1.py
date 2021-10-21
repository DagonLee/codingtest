from collections import deque
n = int(input())
_map = []
for _ in range(n):
	_map.append(input())
norm_check = [[False] * n for _ in range(n)]
color_blind_check = [[False] * n for _ in range(n)]
directions = ((0, 1), (0, -1), (-1, 0), (1, 0))
norm_cnt = 0
color_blind_cnt = 0


def bfs(x, y, c, color_blind: bool):
	color = c
	q = deque([(x, y)])
	check = color_blind_check if color_blind else norm_check
	while q:
		now_x, now_y = q.popleft()
		for dx, dy in directions:
			next_x, next_y = now_x + dx, now_y + dy
			if next_x < 0 or n <= next_x or n <= next_y or next_y < 0:
				continue
			if not check[next_x][next_y]:
				if color_blind:
					if (color == 'R' or color == 'G') and (_map[next_x][next_y] == 'R' or _map[next_x][next_y] == 'G'):
						check[next_x][next_y] = True
						q.append((next_x, next_y))
					elif color == _map[next_x][next_y]:
						check[next_x][next_y] = True
						q.append((next_x, next_y))
				else:
					if _map[next_x][next_y] == color:
						check[next_x][next_y] = True
						q.append((next_x, next_y))


for i in range(n):
	for j in range(n):
		if not norm_check[i][j]:
			norm_check[i][j] = True
			bfs(i, j, _map[i][j], False)
			norm_cnt += 1
		if not color_blind_check[i][j]:
			color_blind_check[i][j] = True
			bfs(i, j, _map[i][j], True)
			color_blind_cnt += 1

print(norm_cnt, color_blind_cnt)