n = int(input())
a = list(map(int, input().split()))
a.sort()
left = 0
right = n - 1
ans = 2 * 1e9
res = [()]
while left < right:
	if left != right and abs(a[left] + a[right]) < abs(ans):
		res.pop()
		res.append((a[left], a[right]))
		ans = a[left] + a[right]
	if a[left] + a[right] < 0:
		left += 1
	else:
		right -= 1
print(res[0][0], res[0][1])