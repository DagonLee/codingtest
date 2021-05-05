import sys
sys.setrecursionlimit(10000000)
n, m = map(int, input().split())
matrix = [list(map(int, list(input()))) for _ in range(n)]
dx = [-1, 0, 0, 1]
dy = [0, -1, 1, 0]


def dfs(i, j, c):
	matrix[i][j] = c
	cnt = 1
	for k in range(4):
		nx, ny = i + dx[k], j + dy[k]
		if 0 <= nx < n and 0 <= ny < m:
			if matrix[nx][ny] == 0:
				cnt += dfs(nx, ny, c)
	return cnt


c = 1
group_dic = dict()
for i in range(n):
	for j in range(m):
		if matrix[i][j] == 0:
			c += 1
			group_dic[c] = dfs(i, j, c)
ans = [[0] * m for _ in range(n)]
for i in range(n):
	for j in range(m):
		adj_group = set()
		if matrix[i][j] == 1:
			for k in range(4):
				nx, ny = i + dx[k], j + dy[k]
				if nx < 0 or n <= nx or ny < 0 or m <= ny:
					continue
				if matrix[nx][ny] != 1:
					adj_group.add(matrix[nx][ny])
			cnt = 1
			for g in adj_group:
				cnt += group_dic[g]
			ans[i][j] = cnt % 10

for i in range(n):
	print(''.join(map(str, ans[i])))
