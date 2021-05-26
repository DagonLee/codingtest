from collections import deque

m, n = map(int, input().split())
mat = [list(map(int, input().split())) for _ in range(n)]
d = [[-1] * m for _ in range(n)]
dx = [0, -1, 0, 1]
dy = [-1, 0, 1, 0]


def bfs(i, j, c):
	cnt = 1
	q = deque()
	q.append((i, j))
	d[i][j] = c
	while q:
		x, y = q.popleft()
		for k in range(4):
			nx, ny = x + dx[k], y + dy[k]
			if nx < 0 or n <= nx or ny < 0 or m <= ny:
				continue
			if mat[x][y] & (1 << k) > 0:
				continue
			if d[nx][ny] == -1:
				cnt += 1
				d[nx][ny] = c
				q.append((nx, ny))
	return cnt


rooms = []
color = 0
max_room = 0
for i in range(n):
	for j in range(m):
		if d[i][j] == -1:
			room_size = bfs(i, j, color)
			rooms.append(room_size)
			if max_room < room_size:
				max_room = room_size
			color += 1

print(len(rooms))
print(max_room)
ans = 0
for i in range(n):
	for j in range(m):
		for k in range(4):
			nx, ny = i + dx[k], j + dy[k]
			if nx < 0 or n <= nx or ny < 0 or m <= ny:
				continue
			if d[i][j] == d[nx][ny]:
				continue
			if mat[i][j] & (1 << k) > 0:
				merge_size = rooms[d[i][j]] + rooms[d[nx][ny]]
				if ans < merge_size:
					ans = merge_size

print(ans)
