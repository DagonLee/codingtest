d = [0] * 1000001
d[0] = 1
for i in range(1, 1000001):
	if i >= 1:
		d[i] += d[i - 1] % 1000000009
	if i >= 2:
		d[i] += d[i - 2] % 1000000009
	if i >= 3:
		d[i] += d[i - 3] % 1000000009
t = int(input())
for i in range(t):
	n = int(input())
	print(d[n] % 1000000009)
