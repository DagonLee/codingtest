n = int(input())
arr = [[0] * n for _ in range(n)]
for i in range(1, n + 1):
	nums = list(map(int, input().split()))
	for j in range(len(nums)):
		arr[i - 1][j] = nums[j]
for i in range(1, n):
	for j in range(n):
		if j != 0:
			arr[i][j] += max(arr[i - 1][j - 1], arr[i - 1][j])
		else:
			arr[i][j] += arr[i - 1][j]

print(max(arr[n - 1]))