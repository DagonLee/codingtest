from collections import deque

n = int(input())
matrix = [list(map(int, input().split())) for _ in range(n)]
time = 0
exp = 0
size = 2
x, y = 0, 0
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]


def bfs(i, j, s):
	ans = []
	visit = [[False] * n for _ in range(n)]
	d = [[0] * n for _ in range(n)]
	q = deque()
	q.append((i, j))
	while q:
		now_x, now_y = q.popleft()
		for k in range(4):
			next_x, next_y = now_x + dx[k], now_y + dy[k]
			if next_x < 0 or n <= next_x or next_y < 0 or n <= next_y:
				continue
			if not visit[next_x][next_y]:
				visit[next_x][next_y] = True
				if matrix[next_x][next_y] > s:
					continue
				elif matrix[next_x][next_y] <= s:
					q.append((next_x, next_y))
					visit[next_x][next_y] = True
					d[next_x][next_y] = d[now_x][now_y] + 1
					if 0 < matrix[next_x][next_y] < s:
						ans.append((d[now_x][now_y] + 1, next_x, next_y))
	if not ans:
		return None
	ans.sort()
	return ans[0]


for i in range(n):
	for j in range(n):
		if matrix[i][j] == 9:
			x = i
			y = j
			matrix[i][j] = 0
while True:
	res = bfs(x, y, size)
	if res is None:
		print(time)
		break
	dist, nx, ny = res
	time += dist
	exp += 1
	if exp == size:
		size += 1
		exp = 0
	matrix[nx][ny] = 0
	x, y = nx, ny
