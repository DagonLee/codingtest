def rec(idx, nums, visit):
	if len(nums) == n + 1:
		check(nums)
		return
	if len(nums) >= 2:
		if op[idx - 2] == '>':
			if nums[idx - 2] < nums[idx - 1]:
				return
		else:
			if nums[idx - 2] > nums[idx - 1]:
				return
	for i in range(10):
		if not visit[i]:
			visit[i] = True
			nums.append(i)
			rec(idx + 1, nums, visit)
			visit[i] = False
			nums.pop()


def check(nums):
	for i in range(len(op)):
		if op[i] == '<':
			if nums[i] > nums[i + 1]:
				return
		else:
			if nums[i] < nums[i + 1]:
				return
	global res_max, res_min
	res_max = max(res_max, int(''.join(map(str, nums))))
	res_min = min(res_min, int(''.join(map(str, nums))))
	return



n = int(input())
op = input().split()
res_max = -1
res_min = 10000000000
visit = [False] * 10
rec(0, [], visit)
if len(str(res_min)) < (n + 1):
	tmp_min = '0' * (n - len(str(res_min)) + 1) + str(res_min)
	res_min = tmp_min

print(res_max)
print(res_min)