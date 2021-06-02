from collections import deque
import sys
n = int(sys.stdin.readline())
q = deque()
for _ in range(n):
	op = sys.stdin.readline().split()
	if op[0] == 'push':
		q.append(int(op[1]))
	elif op[0] == 'front':
		if q:
			print(q[0])
		else:
			print(-1)
	elif op[0] == 'back':
		if q:
			print(q[-1])
		else:
			print(-1)
	elif op[0] == 'empty':
		if q:
			print(0)
		else:
			print(1)
	elif op[0] == 'pop':
		if q:
			print(q.popleft())
		else:
			print(-1)
	elif op[0] == 'size':
		print(len(q))
