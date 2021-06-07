import sys
n, m, store = map(int, sys.stdin.readline().split())
a = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
time = 1e9
ans = 0
for h in range(257):
	plus = 0
	minus = 0
	for i in range(n):
		for j in range(m):
			if a[i][j] > h:
				plus += a[i][j] - h
			else:
				minus += h - a[i][j]
	if store + plus - minus >= 0:
		t = 2 * plus + minus
		if time >= t:
			time = t
			ans = h
print(time, ans)
