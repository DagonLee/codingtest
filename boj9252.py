ans = ''
a = input()
b = input()
a_size = len(a)
b_size = len(b)
a = ' ' + a
b = ' ' + b
d = [[0] * (b_size + 1) for _ in range(a_size + 1)]
v = [[0] * (b_size + 1) for _ in range(a_size + 1)]
for i in range(1, a_size + 1):
	for j in range(1, b_size + 1):
		if a[i] == b[j]:
			d[i][j] = d[i - 1][j - 1] + 1
			v[i][j] = 1
		else:
			if d[i - 1][j] > d[i][j - 1]:
				d[i][j] = d[i - 1][j]
				v[i][j] = 2
			else:
				d[i][j] = d[i][j - 1]
				v[i][j] = 3
print(d[a_size][b_size])
x, y = a_size, b_size
while v[x][y] != 0:
	if v[x][y] == 1:
		ans += a[x]
		x -= 1
		y -= 1
	elif v[x][y] == 2:
		x -= 1
	else:
		y -= 1
print(ans[::-1])