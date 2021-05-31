from collections import defaultdict
x, y, tar = map(int, input().split())
s = [list(map(int, input().split())) for _ in range(3)]
mat = [[0] * 100 for _ in range(100)]
for i in range(3):
	for j in range(3):
		mat[i][j] = s[i][j]
n = 3
m = 3
t = 0


def check():
	if mat[x - 1][y - 1] == tar:
		return True
	return False


while t <= 100:
	if check():
		print(t)
		exit()
	if n >= m:
		mm = m
		for i in range(n):
			d = defaultdict(int)
			for j in range(m):
				if mat[i][j] == 0:
					continue
				d[mat[i][j]] += 1
			tmp = []
			for k, v in d.items():
				tmp.append((v, k))
			tmp.sort()
			l = min(len(tmp), 50)
			for h in range(l):
				mat[i][2 * h] = tmp[h][1]
				mat[i][2 * h + 1] = tmp[h][0]
			for h in range(2 * l, 100):
				mat[i][h] = 0
			if mm < l * 2:
				mm = l * 2
		m = mm
	else:
		nn = n
		for i in range(m):
			d = defaultdict(int)
			for j in range(n):
				if mat[j][i] == 0:
					continue
				d[mat[j][i]] += 1
			tmp = []
			for k, v in d.items():
				tmp.append((v, k))
			tmp.sort()
			l = min(len(tmp), 50)
			for h in range(l):
				mat[2 * h][i] = tmp[h][1]
				mat[2 * h + 1][i] = tmp[h][0]
			for h in range(2 * l, 100):
				mat[h][i] = 0
			if nn < l * 2:
				nn = l * 2
		n = nn
	t += 1
print(-1)
