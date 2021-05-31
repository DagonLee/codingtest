n = int(input())
lst = list(map(int, input().split()))
while n < 3:
	lst += [0]
	n += 1

d = [[[-1] * 61 for i in range(61)] for j in range(61)]


def dfs(i, j, k):
	if i < 0:
		return dfs(0, j, k)
	if j < 0:
		return dfs(i, 0, k)
	if k < 0:
		return dfs(i, j, 0)
	if i == 0 and j == 0 and k == 0:
		return 0
	ans = d[i][j][k]
	if ans != -1:
		return ans
	ans = 1e9
	if ans > dfs(i - 9, j - 3, k - 1):
		ans = dfs(i - 9, j - 3, k - 1)
	if ans > dfs(i - 9, j - 1, k - 3):
		ans = dfs(i - 9, j - 1, k - 3)
	if ans > dfs(i - 3, j - 1, k - 9):
		ans = dfs(i - 3, j - 1, k - 9)
	if ans > dfs(i - 3, j - 9, k - 1):
		ans = dfs(i - 3, j - 9, k - 1)
	if ans > dfs(i - 1, j - 3, k - 9):
		ans = dfs(i - 1, j - 3, k - 9)
	if ans > dfs(i - 1, j - 9, k - 3):
		ans = dfs(i - 1, j - 9, k - 3)
	ans += 1
	d[i][j][k] = ans
	return d[i][j][k]


print(dfs(lst[0], lst[1], lst[2]))
