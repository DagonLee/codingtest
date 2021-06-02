import math
t = int(input())
for _ in range(t):
	ans = 0
	x1, y1, r1, x2, y2, r2 = map(int, input().split())
	d = math.sqrt(pow((x1 - x2), 2) + pow((y1 - y2), 2))
	if d == 0:
		if r1 == r2:
			print(-1)
		else:
			print(0)
	elif d == abs(r1 - r2) or d == r1 + r2:
		print(1)
	elif abs(r1 - r2) < d < r1 + r2:
		print(2)
	elif d > r1 + r2 or d < abs(r1 - r2):
		print(0)
