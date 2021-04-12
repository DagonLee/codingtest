a = input()
b = input()
a_size = len(a)
b_size = len(b)
a = ' ' + a
b = ' ' + b
d = [[0] * (b_size + 1) for _ in range(a_size + 1)]
for i in range(1, a_size + 1):
	for j in range(1, b_size + 1):
		if a[i] == b[j]:
			d[i][j] = d[i - 1][j - 1] + 1
		else:
			d[i][j] = max(d[i - 1][j], d[i][j - 1])
print(d[a_size][b_size])
