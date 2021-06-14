n = int(input())
a = list(map(int, input().split()))


def gcd(a, b):
	while b:
		a, b = b, a % b
	return a


for i in range(1, n):
	print(str(a[0] // gcd(a[0], a[i]))+ '/' + str(a[i] // gcd(a[0], a[i])))