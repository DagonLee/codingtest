from collections import deque
warp = dict()
u, v = map(int, input().split())
for _ in range(u + v):
	s, e = map(int, input().split())
	warp[s] = e
q = deque()
q.append(1)
check = [-1] * 101
check[1] = 0
while q:
	now = q.popleft()
	for k in range(1, 7):
		if now + k <= 100 and check[now + k] == -1:
			check[now + k] = check[now] + 1
			if now + k in warp:
				if check[warp[now + k]] == -1:
					check[warp[now + k]] = check[now] + 1
					q.append(warp[now + k])
			else:
				q.append(now + k)
print(check[100])
