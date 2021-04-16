from collections import deque
from collections import defaultdict
n = int(input())
arr = []
dx = [0, 0, -1, 1]
dy =[-1, 1, 0, 0]
for _ in range(n):
	arr.append(list(map(int, list(input()))))
# dfs solution
ans = []
visit = [[False] * len(arr) for _ in range(len(arr))]


def dfs(i, j):
	cnt = 1
	visit[i][j] = True
	for k in range(4):
		nx, ny = i + dx[k], j + dy[k]
		if nx < 0 or len(arr) <= nx or ny < 0 or len(arr) <= ny:
			continue
		if arr[nx][ny] == 1 and not visit[nx][ny]:
			cnt += dfs(nx, ny)
	return cnt


for i in range(len(arr)):
	for j in range(len(arr[0])):
		if arr[i][j] == 1 and not visit[i][j]:
			ans.append(dfs(i, j))
ans.sort()
print(len(ans))
for i in ans:
	print(i)
# bfs solution
# color = 1
# for i in range(len(arr)):
# 	for j in range(len(arr[0])):
# 		if arr[i][j] == 1:
# 			color += 1
# 			arr[i][j] = color
# 			q = deque()
# 			q.append((i, j))
# 			while q:
# 				x, y = q.popleft()
# 				for k in range(4):
# 					nx, ny = x + dx[k], y + dy[k]
# 					if nx < 0 or len(arr) <= nx or ny < 0 or len(arr[0]) <= ny:
# 						continue
# 					if arr[nx][ny] == 1:
# 						arr[nx][ny] = color
# 						q.append((nx, ny))
# house_cnt = defaultdict(int)
# for i in range(len(arr)):
# 	for j in range(len(arr[0])):
# 		if arr[i][j] != 0:
# 			house_cnt[arr[i][j]] += 1
# ans = list(house_cnt.values())
# ans.sort()
# print(color - 1)
# for i in ans:
# 	print(i)
