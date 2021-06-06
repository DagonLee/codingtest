while True:
	s = input()
	if len(s) == 1 and s[0] == '.':
		break
	stack = []
	ans = True
	for i in s:
		if i == '(':
			stack.append(i)
		elif i == ')':
			if stack and stack[-1] == '(':
				stack.pop()
			else:
				ans = False
				break
		if i == '[':
			stack.append(i)
		elif i == ']':
			if stack and stack[-1] == '[':
				stack.pop()
			else:
				ans = False
				break
	if stack:
		ans = False
	if ans:
		print('yes')
	else:
		print('no')
