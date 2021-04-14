def next_permutation(lst):
	j = len(lst) - 1
	while j > 0 and lst[j] <= lst[j - 1]:
		j -= 1
	if j == 0:
		return False
	i = len(lst) - 1
	while lst[i] <= lst[j - 1]:
		i -= 1
	lst[i], lst[j - 1] = lst[j - 1], lst[i]
	i = len(lst) - 1
	while j < i:
		lst[j], lst[i] = lst[i], lst[j]
		j += 1
		i -= 1
	return True


def prev_permutation(lst):
	j = len(lst) - 1
	while j > 0 and lst[j] >= lst[j - 1]:
		j -= 1
	if j == 0:
		return False
	i = len(lst) - 1
	while lst[i] >= lst[j - 1]:
		i -= 1
	lst[i], lst[j - 1] = lst[j - 1], lst[i]
	i = len(lst) - 1
	while j < i:
		lst[j], lst[i] = lst[i], lst[j]
		j += 1
		i -= 1
	return True


def check(perm, a):
	for i in range(len(a)):
		if a[i] == '<' and perm[i] > perm[i + 1]:
			return False
		if a[i] == '>' and perm[i] < perm[i + 1]:
			return False
	return True


n = int(input())
a = input().split()
small = [i for i in range(n + 1)]
big = [9 - i for i in range(n + 1)]

while True:
	if check(small, a):
		break
	if not next_permutation(small):
		break
while True:
	if check(big, a):
		break
	if not prev_permutation(big):
		break

print(''.join(map(str, big)))
print(''.join(map(str, small)))

