import re


def signal_check(signal):
	return 'YES' if re.search('^(100+1+|01)+$', signal) else 'NO'


for _ in range(int(input())):
	print(signal_check(input()))