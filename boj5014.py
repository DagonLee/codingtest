from collections import deque
f, s, g, u, d = map(int, input().split())
dist = [-1] * (f + 1)
dist[s] = 0
q = deque()
q.append(s)
while q:
	h = q.popleft()
	if 1 <= h - d and dist[h - d] == -1:
		q.append(h - d)
		dist[h - d] = dist[h] + 1
	if h + u <= f and dist[h + u] == -1:
		q.append(h + u)
		dist[h + u] = dist[h] + 1
if dist[g] == -1:
	print('use the stairs')
else:
	print(dist[g])
