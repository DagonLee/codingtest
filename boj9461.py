d = [-1] * 101


def go(n):
	if n <= 3:
		return 1
	elif n <= 5:
		return 2
	elif d[n] != -1:
		return d[n]
	else:
		d[n] = go(n - 1) + go(n - 5)
		return d[n]

t = int(input())
for _ in range(t):
	print(go(int(input())))
