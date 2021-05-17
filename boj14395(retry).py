from collections import deque
s, t = map(int, input().split())
q = deque()
q.append((s, ''))
check = set()
if s == t:
	print(0)
	exit()
while q:
	now, op = q.popleft()
	if now == t:
		print(op)
	if now * now <= (10 ** 9) and now * now not in check:
		check.add(now * now)
		q.append((now * now, op + '*'))
	if now + now <= (10 ** 9) and now + now not in check:
		check.add(now + now)
		q.append((now + now, op + '+'))
	if 0 not in check:
		check.add(0)
		q.append((0, op + '-'))
	if now != 0 and 1 not in check:
		check.add(1)
		q.append((1, op + '/'))

if t not in check:
	print(-1)

