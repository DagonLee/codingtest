from collections import deque
a = []
n, m, t = map(int, input().split())
remove = False


def rot(x, d, k):
	global remove
	remove = False
	for i in range(n):
		if (i + 1) % x == 0:
			if d == 0:
				for _ in range(k):
					a[i].appendleft(a[i].pop())
			else:
				for _ in range(k):
					a[i].append(a[i].popleft())
	d = [[False] * m for _ in range(n)]

	for i in range(n):
		for j in range(m):
			if a[i][j] == a[i][(j + 1) % m] and a[i][j] != 0:
				d[i][j] = d[i][(j + 1) % m] = True
			if i + 1 < n and a[i][j] == a[i + 1][j] and a[i][j] != 0:
				d[i][j] = d[i + 1][j] = True

	for i in range(n):
		for j in range(m):
			if d[i][j]:
				remove = True
				a[i][j] = 0

	if not remove:
		s = 0
		cnt = 0
		for i in range(n):
			s += sum(a[i])
		for i in range(n):
			for j in range(m):
				if a[i][j] != 0:
					cnt += 1
		if cnt == 0:
			return
		avg = s / cnt
		for i in range(n):
			for j in range(m):
				if a[i][j] > avg and a[i][j] != 0:
					a[i][j] -= 1
				elif a[i][j] < avg and a[i][j] != 0:
					a[i][j] += 1


def cal():
	ans = 0
	for i in range(n):
		ans += sum(a[i])
	return ans


for _ in range(n):
	q = deque(list(map(int, input().split())))
	a.append(q)
for _ in range(t):
	x, d, k = map(int, input().split())
	rot(x, d, k)
print(cal())

