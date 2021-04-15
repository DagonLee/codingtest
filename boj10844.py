d = [[0] * 10 for _ in range(101)]
for i in range(1, 10):
	d[1][i] = 1
for i in range(2, 101):
	for k in range(10):
		if k == 0:
			d[i][k] = d[i - 1][1]
		elif k == 9:
			d[i][k] = d[i - 1][8]
		else:
			d[i][k] = d[i - 1][k - 1] + d[i - 1][k + 1]
n = int(input())
print(sum(d[n]) % 1000000000)
