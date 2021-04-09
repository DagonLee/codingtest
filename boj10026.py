from collections import deque
n = int(input())
matrix = [list(input()) for _ in range(n)]
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]
normal = 0


def can(blind, s, e):
	if s == e:
		return True
	if blind:
		if s == 'R' and e == 'G':
			return True
		if s == 'G' and e == 'R':
			return True
	return False


def bfs(blind):
	ans = 0
	check = [[False] * n for _ in range(n)]
	for i in range(n):
		for j in range(n):
			if check[i][j] is False:
				ans += 1
				q = deque()
				q.append((i, j))
				check[i][j] = True
				while q:
					x, y = q.popleft()
					for k in range(4):
						nx, ny = x + dx[k], y + dy[k]
						if nx < 0 or n <= nx or ny < 0 or n <= ny:
							continue
						if can(blind, matrix[x][y], matrix[nx][ny]) and not check[nx][ny]:
							check[nx][ny] = True
							q.append((nx, ny))
	return str(ans)


print(bfs(False) + ' ' + bfs(True))
