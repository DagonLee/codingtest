import sys
n = int(sys.stdin.readline())
cnt = [0] * 10001
for _ in range(n):
	cnt[int(sys.stdin.readline())] += 1
for i in range(1, 10001):
	for j in range(cnt[i]):
		sys.stdout.write(str(i) + '\n')
