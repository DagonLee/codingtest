def zigzag(x, y, size):
	if x == r and y == c:
		global ans
		print(ans)
		return
	if x <= r < x + size and y <= c < y + size:
		zigzag(x, y, size // 2)
		zigzag(x, y + size // 2, size // 2)
		zigzag(x + size // 2, y, size // 2)
		zigzag(x + size // 2, y + size // 2, size // 2)
	else:
		ans += size * size


n, r, c = map(int, input().split())
ans = 0
zigzag(0, 0, 1 << n)

