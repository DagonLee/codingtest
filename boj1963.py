from collections import deque

era = [True] * 10000
era[0] = False
era[1] = False
i = 2
while i * i <= 10000:
	if era[i] is True:
		for j in range(i * i, 10000, i):
			era[j] = False
	i += 1


def change(ans, idx, num):
	res = list(str(ans))
	res[idx] = str(num)
	return ''.join(res)


t = int(input())
for _ in range(t):
	s, e = map(int, input().split())
	q = deque()
	q.append(s)
	visit = [-1] * 10000
	visit[s] = 0
	while q:
		now = q.popleft()
		for i in range(4):
			for n in range(10):
				if i == 0 and n == 0:
					continue
				tmp = change(now, i, n)
				tmp = int(tmp)
				if era[tmp] and visit[tmp] == -1:
					visit[tmp] = visit[now] + 1
					q.append(tmp)
	if visit[e] == -1:
		print('impossible')
	else:
		print(visit[e])
