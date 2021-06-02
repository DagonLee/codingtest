def pal(s):
	for i in range(len(s) // 2):
		if s[i] != s[len(s) - 1 - i]:
			return False
	return True


while True:
	n = input()
	if n == '0':
		break
	else:
		if pal(n):
			print('yes')
		else:
			print('no')

