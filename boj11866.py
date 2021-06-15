from collections import deque
n, k = map(int, input().split())
q = deque([i for i in range(1, n + 1)])
cnt = 1
ans = []
while q:
	if cnt == k:
		ans.append(q.popleft())
		cnt = 1
	else:
		q.append(q.popleft())
		cnt += 1

print('<', end='')
for i in range(len(ans)):
	if i == len(ans) - 1:
		print(str(ans[i]), end='')
	else:
		print(str(ans[i]) + ',', end=' ')
print('>')
