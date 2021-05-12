n = int(input())
lst = list(map(int, input().split()))
d = [[-1] * n for _ in range(n)]


def go(i, j):
	if i == j:
		return 1
	if j - i == 1:
		if lst[i] == lst[j]:
			return 1
		else:
			return 0
	if d[i][j] != -1:
		return d[i][j]
	if lst[i] != lst[j]:
		d[i][j] = 0
	else:
		d[i][j] = go(i + 1, j - 1)
	return d[i][j]


m = int(input())
for _ in range(m):
	s, e = map(int, input().split())
	print(go(s - 1, e - 1))
