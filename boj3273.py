n = int(input())
a = list(map(int, input().split()))
x = int(input())
a.sort()
left = 0
right = n - 1
s = a[0]
ans = 0
while left <= right:
	if a[left] + a[right] <= x:
		if a[left] + a[right] == x and left != right:
			ans += 1
		left += 1
	else:
		right -= 1
print(ans)