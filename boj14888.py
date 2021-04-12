def go(idx, cur, plus, minus, mul, div):
	res = []
	if idx == n:
		return (cur, cur)
	if plus > 0:
		res.append(go(idx + 1, cur + nums[idx], plus - 1, minus, mul, div))
	if minus > 0:
		res.append(go(idx + 1, cur - nums[idx], plus, minus - 1, mul, div))
	if mul > 0:
		res.append(go(idx + 1, cur * nums[idx], plus, minus, mul - 1, div))
	if div > 0:
		if cur >= 0:
			res.append(go(idx + 1, cur // nums[idx], plus, minus, mul, div - 1))
		else:
			res.append(go(idx + 1, -((-cur) // nums[idx]), plus, minus, mul, div - 1))
	ans = (max([t[0] for t in res]), min([t[1] for t in res]))
	return ans


n = int(input())
nums = list(map(int, input().split()))
pl, mi, mu, di = map(int, input().split())
ans = go(1, nums[0], pl, mi, mu, di)
print(ans[0])
print(ans[1])