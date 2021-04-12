a = input()
b = input()
a_size = len(a)
b_size = len(b)
a = ' ' + a
b = ' ' + b
ans = 0
d = [[0] * (b_size + 1) for _ in range(a_size + 1)]
for i in range(1, a_size + 1):
	for j in range(1, b_size + 1):
		if a[i] == b[j]:
			d[i][j] = d[i - 1][j - 1] + 1
for i in range(a_size + 1):
	for j in range(b_size + 1):
		if d[i][j] > ans:
			ans = d[i][j]
print(ans)