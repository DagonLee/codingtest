from collections import deque
n = int(input())
lst = list(map(int, input().split()))
dist = [-1] * n
q = deque()
q.append(0)
dist[0] = 0
while q:
	now = q.popleft()
	for i in range(1, lst[now] + 1):
		if (now + i) < n and dist[now + i] == -1:
			dist[now + i] = dist[now] + 1
			q.append(now + i)
if dist[n - 1] == -1:
	print(-1)
else:
	print(dist[n - 1])
