import sys
sys.setrecursionlimit(1500*1500)
a, b, c = map(int, input().split())
check = [[False] * 1500 for _ in range(1500)]
s = a + b + c


def dfs(a, b):
	if check[a][b]:
		return
	check[a][b] = True
	v = [a, b, s - a - b]
	for i in range(3):
		for j in range(3):
			if v[i] < v[j]:
				nv = [a, b, s - a - b]
				nv[i] += v[i]
				nv[j] -= v[i]
				dfs(nv[0], nv[1])


if s % 3 != 0:
	print(0)
else:
	dfs(a, b)
	if check[s // 3][s // 3]:
		print(1)
	else:
		print(0)
