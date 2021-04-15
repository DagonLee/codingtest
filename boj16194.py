n = int(input())
p = [0] + list(map(int, input().split()))
d = [0] * (n + 1)
d[1] = p[1]
for i in range(2, n + 1):
	d[i] = p[1] + d[i - 1]
	for k in range(2, i + 1):
		d[i] = min(d[i], p[k] + d[i - k])
print(d[n])