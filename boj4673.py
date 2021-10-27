check = [False] * 10001


def self_num(n):
	num = n
	_sum = num
	while num:
		_sum += num % 10
		num //= 10

	if _sum <= 10000:
		check[_sum] = True


for i in range(1, 10001):
	self_num(i)

for i in range(1, 10001):
	if not check[i]:
		print(i)
