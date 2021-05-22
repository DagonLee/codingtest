from collections import deque

n, k = map(int, input().split())
d = [-1] * 100001
q = deque()
q.append(n)
d[n] = 0
while q:
	x = q.popleft()
	if x == k:
		print(d[k])
		exit()
	if 2 * x <= 100000 and d[2 * x] == -1:
		d[2 * x] = d[x]
		q.appendleft(2 * x)
	if x - 1 >= 0 and d[x - 1] == -1:
		d[x - 1] = d[x] + 1
		q.append(x - 1)
	if x + 1 <= 100000 and d[x + 1] == -1:
		d[x + 1] = d[x] + 1
		q.append(x + 1)
