from collections import deque
n = int(input())
lst = list(map(int, input().split()))
nums = [(i + 1, n) for i, n in enumerate(lst)]
q = deque(nums)
ans = []

while q:
	b = q.popleft()
	ans.append(b[0])
	if not q:
		break
	if b[1] > 0:
		for _ in range(b[1] - 1):
			q.append(q.popleft())
	else:
		for _ in range(-b[1]):
			q.appendleft(q.pop())

for i in range(len(ans)):
	print(ans[i], end=' ')
