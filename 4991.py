from collections import deque
from itertools import permutations

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]


def sol(rx, ry, lst):
	ans = 1e9
	per_lst = (list(permutations(range(len(lst)), len(lst))))
	print(per_lst, len(per_lst))
	return ans


def bfs(sx, sy, tx, ty):
	dist = [[-1] * y for _ in range(x)]
	dist[sx][sy] = 0
	q = deque()
	q.append((sx, sy))
	while q:
		now_r, now_c = q.popleft()
		if now_r == tx and now_c == ty:
			return dist[tx][ty]
		for i in range(4):
			new_r, new_c = now_r + dx[i], now_c + dy[i]
			if new_r < 0 or x <= new_r or new_c < 0 or y <= new_c:
				continue
			if (arr[new_r][new_c] == '.' or arr[new_r][new_c] == '*') and dist[new_r][new_c] == -1:
				dist[new_r][new_c] = dist[now_r][now_c] + 1
				q.append((new_r, new_c))
	return dist[tx][ty]


while True:
	y, x = map(int, input().split())
	if y == 0 and x == 0:
		exit()
	arr = [list(input()) for _ in range(x)]
	rx, ry = 0, 0
	lst = []
	for i in range(x):
		for j in range(y):
			if arr[i][j] == 'o':
				rx, ry = i, j
			elif arr[i][j] == '*':
				lst.append((i, j))
	print(sol(rx, ry, lst))








