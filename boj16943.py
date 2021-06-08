from itertools import permutations
a, b = input().split()
a = [str(i) for i in a]
p = list(permutations(a, len(a)))
b = int(b)
ans = -1
for i in p:
	if i[0] == '0':
		continue
	v = int(''.join(i))
	if v <= b and v > ans:
		ans = v
print(ans)