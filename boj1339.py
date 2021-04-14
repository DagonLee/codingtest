from collections import defaultdict
n = int(input())
alp_dic = defaultdict(int)
for _ in range(n):
	word = input()
	k = len(word) - 1
	for alp in word:
		alp_dic[alp] += 10 ** k
		k -= 1
nums = alp_dic.values()
nums = list(nums)
nums.sort(reverse=True)
ans = 0
a = 9
for i in range(len(nums)):
	ans += nums[i] * a
	a -= 1
print(ans)
