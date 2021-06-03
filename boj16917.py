a, b, c, x, y = map(int, input().split())
lim = max(x, y)
ans = 10 ** 10
for i in range(lim + 1):
	tx, ty = x - i, y - i
	if tx <= 0:
		tx = 0
	if ty <= 0:
		ty = 0
	tmp = a * tx + b * ty + 2 * c * i
	if ans > tmp:
		ans = tmp
print(ans)