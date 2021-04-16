n = int(input())
d = [0] * (n + 1)
d[0] = 1
for i in range(n + 1):
	if i >= 2:
		d[i] += 3 * d[i - 2]
	for j in range(4, i + 1):
		if j % 2 == 0:
			d[i] += 2 * d[i - j]

print(d[n])
