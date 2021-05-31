from collections import deque
from itertools import permutations
n = int(input())
scv = list(map(int, input().split()))
while n < 3:
	scv += [0]
	n += 1

d = [[[-1] * 61 for _ in range(61)] for _ in range(61)]
q = deque()
q.append((scv[0], scv[1], scv[2]))
d[scv[0]][scv[1]][scv[2]] = 0
p = list(permutations([1, 3, 9], 3))
while q:
	x, y, z = q.popleft()
	if x == 0 and y == 0 and z == 0:
		print(d[x][y][z])
		break
	for i in p:
		nx, ny, nz = x - i[0], y - i[1], z - i[2]
		if nx < 0:
			nx = 0
		if ny < 0:
			ny = 0
		if nz < 0:
			nz = 0
		if d[nx][ny][nz] == -1:
			d[nx][ny][nz] = d[x][y][z] + 1
			q.append((nx, ny, nz))
