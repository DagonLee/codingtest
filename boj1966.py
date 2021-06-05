from collections import deque
t = int(input())
for _ in range(t):
	n, idx = map(int, input().split())
	imp_q = deque(list(map(int, input().split())))
	idx_q = deque(range(n))
	cnt = 1
	while True:
		if imp_q[0] == max(imp_q):
			if idx_q[0] == idx:
				print(cnt)
				break
			cnt += 1
			imp_q.popleft()
			idx_q.popleft()
			if not imp_q:
				break
		else:
			imp_q.append(imp_q.popleft())
			idx_q.append(idx_q.popleft())
