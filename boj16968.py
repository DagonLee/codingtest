def car(num, idx, prev):
	if idx == len(num):
		return 1
	start = ord('a') if num[idx] == 'c' else ord('0')
	end = ord('z') if num[idx] == 'c' else ord('9')
	ans = 0
	for i in range(start, end + 1):
		if i == prev:
			continue
		ans += car(num, idx + 1, i)
	return ans


s = input()
print(car(s, 0, -1))
