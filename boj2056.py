from collections import deque
n = int(input())
a = [[] for _ in range(n + 1)]
ind = [0] * (n + 1)
d = [0] * (n + 1)
t = [0] * (n + 1)

for i in range(n):
	v = list(map(int, input().split()))
	d[i + 1] = v[0]
	for j in range(v[1]):
		a[v[j + 2]].append(i + 1)
		ind[i + 1] += 1
q = deque()
for i in range(1, n + 1):
	if ind[i] == 0:
		q.append(i)
		t[i] = d[i]
while q:
	x = q.popleft()
	for y in a[x]:
		if t[y] < t[x] + d[y]:
			t[y] = t[x] + d[y]
		ind[y] -= 1
		if ind[y] == 0:
			q.append(y)
print(max(t))
