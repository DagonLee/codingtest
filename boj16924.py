n, m = map(int, input().split())
a = [list(input()) for _ in range(n)]
check = [[False] * m for _ in range(n)]
ans = []
for i in range(n):
	for j in range(m):
		if a[i][j] == '*':
			s = 1
			while True:
				if 0 <= i - s and i + s < n and 0 <= j - s and j + s < m:
					if a[i - s][j] == '*' and a[i + s][j] == '*' and a[i][j - s] == '*' and a[i][j + s] == '*':
						check[i][j] = True
						check[i - s][j] = True
						check[i + s][j] = True
						check[i][j - s] = True
						check[i][j + s] = True
						ans.append((i, j, s))
						s += 1
					else:
						break
				else:
					break

for i in range(n):
	for j in range(m):
		if a[i][j] == '*' and not check[i][j]:
			print(-1)
			exit()
print(len(ans))
for i, j, k in ans:
	print(i + 1, j + 1, k)
