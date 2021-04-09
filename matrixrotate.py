dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
arr = 	[[1, 2, 3, 4, 5],
		 [6, 7, 8, 9, 10],
		 [11, 12, 13, 14, 15],
		 [16, 17, 18, 19, 20]]


def rotate(sx, sy, ex, ey, m):
	if sx - ex == 0 or sy - ey == 0:
		return
	prev = arr[sx][sy]
	if m == 1:
		arr[sx][sy] = arr[sx + 1][sy]
	else:
		arr[sx][sy] = arr[sx][sy + 1]
	x, y = sx, sy + 1
	d = 0
	while sx != x or sy != y:
		tmp = arr[x][y]
		arr[x][y] = prev
		prev = tmp
		x, y = x + dx[d], y + dy[d]
		if x < sx or ex < x or y < sy or ey < y:
			x, y = x - dx[d], y - dy[d]
			d = (d + m) % 4
			x, y = x + dx[d], y + dy[d]


for i in arr:
	print(i)
print()
rotate(0, 0, 1, 1,3)
for i in arr:
	print(i)