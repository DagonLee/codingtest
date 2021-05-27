from collections import deque
cnt = [0, 0, 0]
tmp = []
for i in range(3):
	s = input().split()
	n = int(s[0])
	if n > 0:
		tmp.append(s[1])
	else:
		tmp.append('')
	for j in range(n):
		cnt[ord(s[1][j]) - ord('A')] += 1

d = dict()
d[tuple(tmp)] = 0
q = deque()
q.append(tuple(tmp))
while q:
	x = q.popleft()
	x = list(x)
	for i in range(3):
		for j in range(3):
			if i == j:
				continue
			if len(x[i]) == 0:
				continue
			y = x[:]
			y[j] = y[j] + y[i][-1]
			y[i] = y[i][:-1]
			y = tuple(y)
			if y not in d:
				d[y] = d[tuple(x)] + 1
				q.append(y)

ans = []
for i in range(3):
	n = cnt[i]
	ans.append(chr(ord('A') + i) * n)

print(d[tuple(ans)])
