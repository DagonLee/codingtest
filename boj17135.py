from copy import deepcopy
from itertools import combinations
n, m, d = map(int, input().split())
mat = [list(map(int,input().split())) for _ in range(n)]
mat.append([0] * m)
c = list(combinations(range(m), 3))
e = []
for i in range(n):
	for j in range(m):
		if mat[i][j] == 1:
			e.append([i, j])
e.sort(key=lambda x: (-x[0], x[0]))


def fin_check(arr):
	if not arr:
		return True
	for i in range(len(arr)):
		if arr[i][0] != -1:
			return False
	return True


def sim(x, y, z):
	ene = deepcopy(e)
	c_mat = deepcopy(mat)
	c_mat[n][x] = 2
	c_mat[n][y] = 2
	c_mat[n][z] = 2
	arc = [x, y, z]
	res = 0
	while True:
		eli = set()
		for t in range(3):
			tmp_dis = 30
			tmp_idx = -1
			for i in range(len(ene)):
				if ene[i][0] != -1 and ene[i][1] != -1:
					dis = abs(n - ene[i][0]) + abs(arc[t] - ene[i][1])
					if dis <= d and dis < tmp_dis:
						tmp_idx = i
						tmp_dis = dis
			if tmp_idx != -1:
				eli.add(tmp_idx)
		if eli:
			for l in eli:
				res += 1
				ene[l][0] = -1
				ene[l][1] = -1
		for i in range(len(ene)):
			if ene[i][0] != -1 and ene[i][1] != -1:
				if ene[i][0] + 1 == n:
					ene[i][0] = -1
					ene[i][1] = -1
				else:
					ene[i][0] += 1
		if fin_check(ene):
			break
	return res


ans = -1
for i, j, k in c:
	res = sim(i, j, k)
	if ans == -1 or ans < res:
		ans = res
print(ans)
