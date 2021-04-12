def go(idx, save, lst, s):
	if idx == len(lst):
		if save == s:
			global ans
			ans += 1
		return
	go(idx + 1, save + lst[idx], lst, s)
	go(idx + 1, save, lst, s)


n, s = map(int, input().split())
lst = list(map(int, input().split()))
ans = 0
go(0, 0, lst, s)
if s == 0:
	ans -= 1
print(ans)