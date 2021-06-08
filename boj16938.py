n, l, r, x = map(int, input().split())
a = list(map(int, input().split()))


def go(idx, lst):
	ans = 0
	if idx == len(a):
		if l <= sum(lst) <= r and max(lst) - min(lst) >= x:
			return 1
		return 0
	ans += go(idx + 1, lst + [a[idx]])
	ans += go(idx + 1, lst)
	return ans


print(go(0, []))
