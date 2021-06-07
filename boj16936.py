n = int(input())
a = list(map(int, input().split()))
d = dict()
for i in range(len(a)):
	cnt = 0
	if a[i] % 3 == 0:
		v = a[i]
		while v:
			if v % 3 == 0:
				v //= 3
				cnt += 1
			else:
				break
		d[a[i]] = cnt
	else:
		d[a[i]] = 0
a.sort(key=lambda x: (-d[x], x))
print(' '.join(map(str, a)))
