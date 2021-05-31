d = [0] * 5001
d[0] = 1
for l in range(2, 5001):
	if l % 2 == 0:
		for i in range(2, l + 1, 2):
			d[l] += d[i - 2] % 1000000007 * d[l - i] % 1000000007
n = int(input())
for _ in range(n):
	t = int(input())
	print(d[t] % 1000000007)