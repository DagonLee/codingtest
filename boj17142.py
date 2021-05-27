from itertools import combinations
from collections import deque
n, m = map(int, input().split())
mat = [list(map(int, input().split())) for _ in range(n)]
v_lst = []
for i in range(n):
	for j in range(n):
		if mat[i][j] == 2:
			v_lst.append((i, j))
			mat[i][j] = 0

comb_lst = combinations(range(len(v_lst)), m)
dx = [-1, 0, 0, 1]
dy = [0, -1, 1, 0]


def bfs(com):
	cnt = -1
	q = deque()
	d = [[-1] * n for _ in range(n)]
	for i in com:
		q.append(v_lst[i])
		d[v_lst[i][0]][v_lst[i][1]] = 0
	while q:
		x, y = q.popleft()
		for k in range(4):
			nx, ny = x + dx[k], y + dy[k]
			if nx < 0 or n <= nx or ny < 0 or n <= ny:
				continue
			if mat[nx][ny] == 0 and d[nx][ny] == -1:
				d[nx][ny] = d[x][y] + 1
				q.append((nx, ny))
	for i in range(n):
		for j in range(n):
			if mat[i][j] == 0 and d[i][j] == -1:
				return -1
			elif cnt < d[i][j]:
				cnt = d[i][j]
	return cnt

ans = 2500
for c in comb_lst:
	tmp = bfs(c)
	if tmp != -1 and tmp < ans:
		ans = tmp

if ans == 2500:
	print(-1)
	exit()
print(ans)
