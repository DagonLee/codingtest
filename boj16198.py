n = int(input())
marble_list = list(map(int, input().split()))


def go(marble):
	ans = 0
	if len(marble) == 2:
		return 0
	for i in range(1, len(marble) - 1):
		energy = marble[i - 1] * marble[i + 1]
		energy += go(marble[:i] + marble[i + 1:])
		if ans < energy:
			ans = energy
	return ans


print(go(marble_list))
