from collections import deque
n = int(input())
_map = list()
ans = 0
cnt = list()
visit = [[False] * n for _ in range(n)]
for _ in range(n):
	_map.append(input())

dx = [-1, 0, 0, 1]
dy = [0, -1, 1, 0]


def bfs(x, y):
	q = deque([(x, y)])
	cnt = 1
	while q:
		now_x, now_y = q.popleft()
		for d in range(4):
			next_x, next_y = now_x + dx[d], now_y + dy[d]
			if 0 <= next_x < n and 0 <= next_y < n:
				if _map[next_x][next_y] == '1' and not visit[next_x][next_y]:
					visit[next_x][next_y] = True
					q.append((next_x, next_y))
					cnt += 1
	return cnt


for i in range(n):
	for j in range(n):
		if _map[i][j] == '1' and not visit[i][j]:
			visit[i][j] = True
			ans += 1
			cnt.append(bfs(i, j))

print(ans)
cnt.sort()
for i in range(len(cnt)):
	print(cnt[i])