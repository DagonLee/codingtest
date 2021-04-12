def go(idx, lst, ans):
	if len(ans) == 6:
		print(' '.join(map(str, ans)))
		return
	if idx == len(lst):
		return
	go(idx + 1, lst, ans + [lst[idx]])
	go(idx + 1, lst, ans)


while True:
	s = list(map(int, input().split()))
	if s[0] == 0:
		break
	nums = s[1:]
	go(0, nums, [])
	print()
