d = [0] * 11
d[0] = 1
for i in range(11):
	if i >= 1:
		d[i] += d[i - 1]
	if i >= 2:
		d[i] += d[i - 2]
	if i >= 3:
		d[i] += d[i - 3]
t = int(input())
for _ in range(t):
	n = int(input())
	print(d[n])
