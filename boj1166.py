import math
n, l, w, h = map(int, input().split())
left = 0
right = max(l, w, h)
while left <= right:
	mid = (left + right) / 2
	num = (l // mid) * (w // mid) * (h // mid)
	if num >= n:
		left = mid
	else:
		right = mid
	if math.isclose(right, left):
		break
print("%.10f" %(right))
