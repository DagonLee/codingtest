import sys
sys.setrecursionlimit(100000)
n = int(sys.stdin.readline())
lst = list(map(int,sys.stdin.readline().split()))
d = [[-1] * n for _ in range(n)]


def go(i, j):
	if i == j:
		return 1
	if i + 1 == j:
		if lst[i] == lst[j]:
			return 1
		else:
			return 0
	if d[i][j] >= 0:
		return d[i][j]
	else:
		if lst[i] != lst[j]:
			d[i][j] = 0
		else:
			d[i][j] = go(i + 1, j - 1)
		return d[i][j]


m = int(sys.stdin.readline())
for _ in range(m):
	s, e = map(int, sys.stdin.readline().split())
	print(go(s - 1, e - 1))