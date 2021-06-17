def wb(x, y, size):
	if size == 1:
		if a[x][y] == 0:
			return (1, 0)
		else:
			return(0, 1)
	w, b = 0, 0
	for i in range(x, x + size):
		for j in range(y, y + size):
			if a[i][j] == 0:
				w += 1
			else:
				b += 1
	if w == size * size:
		return (1, 0)
	elif b == size * size:
		return (0, 1)
	else:
		n = size // 2
		w1, b1 = wb(x, y, n)
		w2, b2 = wb(x + n, y, n)
		w3, b3 = wb(x, y + n, n)
		w4, b4 = wb(x + n, y + n, n)
		w = w1 + w2 + w3 + w4

		b = b1 + b2 + b3 + b4
		return (w, b)


n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]
ans = wb(0, 0, n)
print(ans[0])
print(ans[1])