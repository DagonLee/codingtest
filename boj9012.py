def ps(s):
	state = 0
	for i in s:
		if i == ')':
			state -= 1
		elif i == '(':
			state += 1
		if state == -1:
			return False
	if state > 0:
		return False
	return True


n = int(input())
for _ in range(n):
	if ps(input()):
		print('YES')
	else:
		print('NO')
