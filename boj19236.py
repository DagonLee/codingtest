from copy import deepcopy
dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, -1, -1, -1, 0, 1, 1, 1]


def shark(num, direction, x, y, d):
	for who in range(1, 17):
		check = False
		for i in range(4):
			for j in range(4):
				if num[i][j] == who:
					for k in range(8):
						nx, ny = i + dx[direction[i][j]], j + dy[direction[i][j]]
						if 0 <= nx < 4 and 0 <= ny < 4 and num[nx][ny] >= 0 and (not (nx == x and ny == y)):
							num[i][j], num[nx][ny] = num[nx][ny], num[i][j]
							direction[i][j], direction[nx][ny] = direction[nx][ny], direction[i][j]
							check = True
							break
						else:
							direction[i][j] += 1
							direction[i][j] %= 8
				if check:
					break
			if check:
				break
	res = 0
	sx, sy = x + dx[d], y + dy[d]
	while 0 <= sx < 4 and 0 <= sy < 4:
		if num[sx][sy] != 0:
			tmp = num[sx][sy]
			num[sx][sy] = 0
			cur = tmp + shark(deepcopy(num), deepcopy(direction), sx, sy, direction[sx][sy])
			if res < cur:
				res = cur
			num[sx][sy] = tmp
		sx += dx[d]
		sy += dy[d]
	return res


n = 4
num = [[0]*n for _ in range(n)]
direction = [[0]*n for _ in range(n)]

for i in range(n):
	temp = list(map(int,input().split()))
	for j in range(n):
		num[i][j] = temp[2*j]
		direction[i][j] = temp[2*j+1]
		direction[i][j] -= 1
ans = num[0][0]
num[0][0] = 0
ans += shark(num, direction, 0, 0, direction[0][0])


print(ans)
