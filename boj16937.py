from itertools import combinations
h, w = map(int, input().split())
n = int(input())
lst = []
for _ in range(n):
	lst.append(list(map(int, input().split())))

c = list(combinations(lst, 2))
ans = 0


def check(a, b):
	if (max(a[0], b[0]) <= h and a[1] + b[1] <= w) or (a[0] + b[0] <= h and max(a[1], b[1]) <= w):
		return True
	if (max(a[1], b[0]) <= h and a[0] + b[1] <= w) or (a[1] + b[0] <= h and max(a[0], b[1]) <= w):
		return True
	if (max(a[0], b[1]) <= h and a[1] + b[0] <= w) or (a[0] + b[1] <= h and max(a[1], b[0]) <= w):
		return True
	if (max(a[1], b[1]) <= h and a[0] + b[0] <= w) or (a[1] + b[1] <= h and max(a[0], b[0]) <= w):
		return True
	return False


for i in range(len(c)):
	a, b = c[i]
	if check(a, b):
		if ans < a[0] * a[1] + b[0] * b[1]:
			ans = a[0] * a[1] + b[0] * b[1]
print(ans)