import itertools
t, e, w, s, n = map(int, input().split())

probability = [e, w, s, n]
probability = [d * 0.01 for d in probability]
visit = [[False] * 29 for _ in range(29)]
directions = ((0, 1), (0, -1), (1, 0), (-1, 0))
result = 0


def dfs(x, y, depth, percent):
	if depth == t:
		global result
		result += percent
		return

	visit[x][y] = True
	for i in range(4):
		next_x = x + directions[i][0]
		next_y = y + directions[i][1]
		if not visit[next_x][next_y]:
			dfs(next_x, next_y, depth + 1, percent * probability[i])
	visit[x][y] = False


dfs(14, 14, 0, 1.0)
print(result)