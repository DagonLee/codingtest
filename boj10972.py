n = int(input())
lst = list(map(int, input().split()))


def next_permutation(lst):
	j = len(lst) - 1
	while j > 0 and lst[j - 1] >= lst[j]:
		j -= 1
	if j == 0:
		return False
	i = len(lst) - 1
	while lst[i] <= lst[j - 1]:
		i -= 1
	lst[i], lst[j - 1] = lst[j - 1], lst[i]
	i = len(lst) - 1
	while j < i:
		lst[i], lst[j] = lst[j], lst[i]
		j += 1
		i -= 1
	return True


if next_permutation(lst):
	for i in lst:
		print(i, end=' ')
else:
	print(-1)