from collections import deque

f, s, g, u, d = map(int, input().split())
p = [-1] * (f + 1)
q = deque()
q.append(s)
p[s] = 0

while q:
	now = q.popleft()
	if now + u <= f and p[now + u] == -1:
		p[now + u] = p[now] + 1
		q.append(now + u)
	if now - d > 0 and p[now - d] == -1:
		p[now - d] = p[now] + 1
		q.append(now - d)

if p[g] == -1:
	print('use the stairs')
else:
	print(p[g])
