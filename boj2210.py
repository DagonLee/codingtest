import sys
sys.setrecursionlimit(1000000)
dx = [-1, 0, 0, 1]
dy = [0, -1, 1, 0]
a = [list(map(int, input().split())) for _ in range(5)]
ans = set()


def dfs(x, y, n, l):
	if l == 6:
		ans.add(n)
		return
	for k in range(4):
		nx, ny = x + dx[k], y + dy[k]
		if nx < 0 or 5 <= nx or ny < 0 or 5 <= ny:
			continue
		dfs(nx, ny, n * 10 + a[nx][ny], l + 1)


for i in range(5):
	for j in range(5):
		dfs(i, j, a[i][j], 1)

print(len(ans))