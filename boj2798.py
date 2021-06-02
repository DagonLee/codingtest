from itertools import combinations

n, m = map(int, input().split())
a = list(map(int, input().split()))
c = list(combinations(a, 3))
ans = 0
for i in c:
	s = sum(i)
	if s <= m and m - s < m - ans:
		ans = s
print(ans)