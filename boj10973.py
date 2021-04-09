n = int(input())
lst = list(map(int, input().split()))


def prev_permutation(lst):
	i = len(lst) - 1
	while 0 < i and lst[i - 1] <= lst[i]:
		i -= 1
	if i == 0:
		return False
	j = len(lst) - 1
	while lst[j] >= lst[i - 1]:
		j -= 1
	lst[i - 1], lst[j] = lst[j], lst[i - 1]
	j = len(lst) - 1
	while i < j:
		lst[i], lst[j] = lst[j], lst[i]
		i += 1
		j -= 1
	return True


if prev_permutation(lst):
	for i in lst:
		print(i, end=' ')
else:
	print(-1)