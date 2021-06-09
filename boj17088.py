n = int(input())
a = list(map(int, input().split()))
if n == 1:
	print(0)
	exit()
ans = -1
for i in range(-1, 2):
	for j in range(-1, 2):
		check = True
		change = 0
		if i != 0:
			change += 1
		if j != 0:
			change += 1
		b = a[0] + i
		c = a[1] + j
		d = c - b
		an = b + d
		for k in range(2, n):
			an += d
			if an == a[k]:
				continue
			elif an == a[k] - 1:
				change += 1
			elif an == a[k] + 1:
				change += 1
			else:
				check = False
				break
		if check:
			if ans == -1 or ans > change:
				ans = change

print(ans)