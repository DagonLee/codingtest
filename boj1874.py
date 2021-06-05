n = int(input())
lst = []
for _ in range(n):
	lst.append(int(input()))
stack =[]
ans = []
m = 0
for i in range(len(lst)):
	if not stack or m < lst[i]:
		for j in range(m + 1, lst[i] + 1):
			ans.append('+')
			stack.append(j)
		stack.pop()
		m = lst[i]
		ans.append('-')
	elif stack[-1] == lst[i]:
		stack.pop()
		ans.append('-')
	elif stack[-1] > lst[i]:
		print('NO')
		exit()
for i in ans:
	print(i)