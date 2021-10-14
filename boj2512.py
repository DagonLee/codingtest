n = int(input())
nums = list(map(int, input().split()))
limit = int(input())
left = 1
right = max(nums)

while left <= right:
	mid = (left + right) // 2
	bucket = 0
	for n in nums:
		bucket += min(n, mid)
	if bucket > limit:
		right = mid - 1
	else:
		left = mid + 1
print(right)