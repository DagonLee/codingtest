def go(idx, s, n, nums):
	if idx == n:
		global lst
		lst.append(s)
		return
	go(idx + 1, s + nums[idx], n, nums)
	go(idx + 1, s, n, nums)


n = int(input())
nums = list(map(int, input().split()))
lst = []
go(0, 0, n, nums)
lst = list(set(lst))
lst.sort()
print_check = False
for i in range(1, len(lst)):
	if i != lst[i]:
		print(i)
		print_check = True
		break
if not print_check:
	print(lst[-1] + 1)