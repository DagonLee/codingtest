n = int(input())
check = [False] * 1001
for i in range(n + 1):
	for j in range(n + 1 - i):
		for k in range(n + 1 - i - j):
			l = n - i - j - k
			res = i * 1 + 5 * j + 10 * k + 50 * l
			check[res] = True
ans = 0
for i in range(1001):
	if check[i]:
		ans += 1

print(ans)