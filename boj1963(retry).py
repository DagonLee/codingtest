from collections import deque
n = int(input())
era = [True] * 10000
i = 2
while i * i < 10000:
	if era[i]:
		for j in range(i * i, 10000, i):
			era[j] = False
	i += 1

for _ in range(n):
	check = [-1] * 10000
	s, e = input().split()
	if s == e:
		print(0)
		continue
	check[int(s)] = 0
	q = deque()
	q.append(s)
	while q:
		x = q.popleft()
		for k in range(4):
			for j in range(10):
				if k == 0 and j == 0:
					continue
				if j == int(s[k]):
					continue
				else:
					new = list(x)
					new[k] = str(j)
					new = ''.join(new)
					if era[int(new)] and check[int(new)] == -1:
						check[int(new)] = check[int(x)] + 1
						q.append(new)
	if check[int(e)] == -1:
		print('impossible')
	else:
		print(check[int(e)])
