n, k = map(int, input().split())
m = [list(map(int, input().split())) for _ in range(n)]
a = [[[] for i in range(n)] for j in range(n)]
where = [None] * k
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]


class Piece:
	def __init__(self, no, direction):
		self.no = no
		self.direction = direction


def opposite(direction):
	if direction == 0:
		return 1
	if direction == 1:
		return 0
	if direction == 2:
		return 3
	return 2


def go(a, where, x, y, nx, ny):
	for p in a[x][y]:
		a[nx][ny].append(p)
		where[p.no] = (nx, ny)
	a[x][y].clear()


for i in range(k):
	x, y, d = map(int, input().split())
	where[i] = (x - 1, y - 1)
	a[x - 1][y - 1].append(Piece(i, d - 1))

for t in range(1, 1001):
	for i in range(k):
		x, y = where[i]
		if a[x][y][0].no == i:
			direction = a[x][y][0].direction
			nx = x + dx[direction]
			ny = y + dy[direction]
			if 0 <= nx < n and 0 <= ny < n:  # in
				if m[nx][ny] == 2:
					a[x][y][0].direction = opposite(direction)
			else:
				a[x][y][0].direction = opposite(direction)
			direction = a[x][y][0].direction
			nx = x + dx[direction]
			ny = y + dy[direction]

			if 0 <= nx < n and 0 <= ny < n:  # in
				if m[nx][ny] == 0:
					go(a, where, x, y, nx, ny)
				elif m[nx][ny] == 1:
					a[x][y].reverse()
					go(a, where, x, y, nx, ny)
				if len(a[nx][ny]) >= 4:
					print(t)
					exit(0)
			else:  # out
				pass
print(-1)
