from collections import deque
t = int(input())
for _ in range(t):
	n, idx = map(int, input().split())
	lst = list(map(int, input().split()))
	q = deque()
	for i, j in enumerate(lst):
		q.append((i, j))
	lst.sort()
	cnt = 1
	while q:
		if q[0][1] == lst[-1]:
			if q[0][0] == idx:
				print(cnt)
				break
			cnt += 1
			lst.pop()
			q.popleft()
		else:
			q.append(q.popleft())
