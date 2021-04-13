n = int(input())


def go(x):
	if x == n:
		global ans
		ans += 1
		return
	for j in range(n):
		if col_check[j]:
			continue
		if diag_check1[x + j]:
			continue
		if diag_check2[j - x + n]:
			continue
		col_check[j] = True
		diag_check1[x + j] = True
		diag_check2[j - x + n] = True
		go(x + 1)
		col_check[j] = False
		diag_check1[x + j] = False
		diag_check2[j - x + n] = False


col_check = [False] * n
diag_check1 = [False] * (2 * n - 1)
diag_check2 = [False] * (2 * n)
ans = 0
go(0)
print(ans)