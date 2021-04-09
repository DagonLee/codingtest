dx = [0, 0, 1, 1, 1, -1, -1, -1]
dy = [-1,1, 0, -1, 1, 0, 1, -1]
n, m, k = map(int, input().split())
ene = [list(map(int, input().split())) for _ in range(n)]
tree = [[[] for _ in range(n)] for _ in range(n)]
land = [[5] * n for _ in range(n)]
cnt = 0
for _ in range(m):
	i, j, a = map(int, input().split())
	tree[i - 1][j - 1].append(a)
while k:
	plant = [[0] * n for _ in range(n)]
	for i in range(n):
		for j in range(n):
			tmp = []
			tree[i][j].sort()
			dead = 0
			for t in tree[i][j]:
				if t <= land[i][j]:
					land[i][j] -= t
					tmp.append(t + 1)
					if (t + 1) % 5 == 0:
						for v in range(8):
							nr, nc = i + dx[v], j + dy[v]
							if nr < 0 or n <= nr or nc < 0 or n <= nc:
								continue
							plant[nr][nc] += 1
				else:
					dead += (t // 2)
			tree[i][j] = tmp
			land[i][j] += dead

	for i in range(n):
		for j in range(n):
			if plant[i][j] > 0:
				for _ in range(plant[i][j]):
					tree[i][j].append(1)
			land[i][j] += ene[i][j]
	k -= 1

for i in range(n):
	for j in range(n):
		cnt += len(tree[i][j])
print(cnt)