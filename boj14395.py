from collections import deque

s, t = map(int, input().split())

q = deque()
q.append((s, ''))
check = set()
check.add(s)
while q:
	n, ans = q.popleft()
	if n == t:
		if len(ans) == 0:
			ans = '0'
		print(ans)
		exit()
	if n * n <= t and n * n not in check:
		q.append((n * n, ans + '*'))
		check.add(n * n)
	if n + n <= t and n + n not in check:
		q.append((n + n, ans + '+'))
		check.add(n + n)
	if 0 not in check:
		q.append((0, ans + '-'))
		check.add(0)
	if n != 0 and 1 <= t and 1 not in check:
		q.append((1, ans + '/'))
		check.add(1)
print(-1)
