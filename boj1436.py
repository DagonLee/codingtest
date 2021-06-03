n = int(input())
ans = 0
cnt = 0
def check(i):
	if '666' in str(i):
		return True
	else:
		return False


while True:
	if check(ans):
		cnt += 1
		if cnt == n:
			print(ans)
			break
	ans += 1

