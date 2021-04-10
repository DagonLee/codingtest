t = int(input())
d = [0] * 10001
nums = [1, 2, 3]
d[0] = 1
for j in range(len(nums)):
	for i in range(1, 10001):
		if i - nums[j] >= 0:
			d[i] += d[i - nums[j]]
while t:
	n = int(input())
	print(d[n])
	t -= 1
