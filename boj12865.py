n, k = map(int, input().split())
w = [0]
v = [0]
for _ in range(n):
	x, y = map(int, input().split())
	w.append(x)
	v.append(y)

d = [0] * (k + 1)

for i in range(1, n + 1):
	for j in range(k, 0, -1):
		if j - w[i] >= 0:
			d[j] = max(d[j], d[j - w[i]] + v[i])

print(d[k])