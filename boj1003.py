d = [0] * 41
d[1] = 1
for i in range(2, 41):
	d[i] = d[i - 2] + d[i - 1]

t = int(input())
for _ in range(t):
	n = int(input())
	if n == 0:
		print(1, 0)
	else:
		print(d[n - 1], d[n])
