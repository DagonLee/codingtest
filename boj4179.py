'not completed'
from collections import deque
import copy

r, c = map(int, input().split())
matrix = []
start_x, start_y = 0, 0
fire_x, fire_y = 0, 0
directions = ((0, 1), (0, -1), (1, 0), (-1, 0))
time = 0
out = False
for _ in range(r):
	matrix.append(input())
for i in range(r):
	for j in range(c):
		if matrix[i][j] == 'J':
			start_x, start_y = i, j
		if matrix[i][j] == 'F':
			fire_x, fire_y = i, j

q = deque([(start_x, start_y, matrix)])
while q:
	now_x, now_y, mat = q.popleft()
	if now_x == 0 or now_x == r - 1 or now_y == 0 or now_y == c - 1:
		out = True
		break
	for i in range(r):
		for j in range(c):
			if mat[i][j] == 'F':
				for dx, dy in directions:
					next_x, next_y = now_x + dx, now_y + dy
					if next_x < 0 or r <= next_x or next_y < 0 or c <= next_y:
						continue
					if mat[next_x][next_y] ==
	for dx, dy in directions:
		next_x, next_y = now_x + dx, now_y + dy
		if next_x < 0 or r <= next_x or next_y < 0 or c <= next_y:
			continue
		if mat[next_x][next_y] == '.':
			new_mat = copy.deepcopy(mat)
