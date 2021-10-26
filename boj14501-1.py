def go(day):
	if day == n:
		return 0
	if day > n:
		return -1e9
	t1 = go(day + 1)
	t2 = go(day + t[day]) + p[day]
	d[day] = max(t1, t2)
	return d[day]


n = int(input())
t = [0] * n
p = [0] * n
d = [0] * n
for i in range(n):
	t[i], p[i] = map(int, input().split())
print(go(0))
