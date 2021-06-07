from collections import deque
n, m = map(int, input().split())
s = [[] for _ in range(n + 1)]
ind = [0] * (n + 1)
q = deque()
for _ in range(m):
	i, j = map(int, input().split())
	s[i].append(j)
	ind[j] += 1

for i in range(1, n + 1):
	if ind[i] == 0:
		q.append(i)

while q:
	x = q.popleft()
	print(x, end=' ')
	for y in s[x]:
		ind[y] -= 1
		if ind[y] == 0:
			q.append(y)
