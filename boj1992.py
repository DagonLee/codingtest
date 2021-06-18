def quad(x, y, size):
	w, b = 0, 0
	ans = ''
	for i in range(x, x + size):
		for j in range(y, y + size):
			if a[i][j] == '0':
				w += 1
			else:
				b += 1
	if w == size * size:
		ans += '0'
	elif b == size * size:
		ans += '1'
	else:
		ans += '('
		ans += quad(x, y, size // 2)
		ans += quad(x, y + size // 2, size // 2)
		ans += quad(x + size // 2, y, size // 2)
		ans += quad(x + size // 2, y + size // 2, size //2)
		ans += ')'
		return ans
	return ans


n = int(input())
a = []
for _ in range(n):
	a.append(list(input()))
print(quad(0, 0, n))