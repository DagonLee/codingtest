def go(day):
	if day == n:
		return 0
	if day > n:
		return -1e9
	if d[day] != -1:
		return d[day]
	ans1 = go(day + t[day]) + p[day]
	ans2 = go(day + 1)
	d[day] = max(ans1, ans2)
	return d[day]


n = int(input())
t = [0] * n
p = [0] * n
d = [-1] * n
for i in range(n):
	t[i], p[i] = map(int, input().split())
print(go(0))
