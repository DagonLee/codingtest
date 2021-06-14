from itertools import permutations
from copy import deepcopy
n, m, k = map(int, input().split())
mat = [list(map(int, input().split())) for _ in range(n)]
op = []
for _ in range(k):
	op.append(list(map(int, input().split())))

op = [(i - 1, j - 1, c) for i, j, c in op]
p = list(permutations(op, k))


def go(a, t):
	row, col, size = t
	groups = []
	for s in range(1, size+1):
		group = []
		# (r-s, c-s) -> (r-s, c+s)
		for c in range(col-s, col+s):
			group.append(a[row-s][c])
		# (r-s, c+s) -> (r+s, c+s)
		for r in range(row-s, row+s):
			group.append(a[r][col+s])
		# (r+s, c+s) -> (r+s, c-s)
		for c in range(col+s, col-s, -1):
			group.append(a[row+s][c])
		# (r+s, c-s) -> (r-s, c-s)
		for r in range(row+s, row-s, -1):
			group.append(a[r][col-s])
		groups.append(group)
	for s in range(1, size+1):
		group = groups[s-1]
		group = group[-1:] + group[:-1]
		index = 0
		# (r-s, c-s) -> (r-s, c+s)
		for c in range(col-s, col+s):
			a[row-s][c] = group[index]
			index += 1
		# (r-s, c+s) -> (r+s, c+s)
		for r in range(row-s, row+s):
			a[r][col+s] = group[index]
			index += 1
		# (r+s, c+s) -> (r+s, c-s)
		for c in range(col+s, col-s, -1):
			a[row+s][c] = group[index]
			index += 1
		# (r+s, c-s) -> (r-s, c-s)
		for r in range(row+s, row-s, -1):
			a[r][col-s] = group[index]
			index += 1


ans = 10000
for t in range(len(p)):
	a = deepcopy(mat)
	for i in p[t]:
		go(a, i)
	for j in range(n):
		s = sum(a[j])
		if s < ans:
			ans = s

print(ans)