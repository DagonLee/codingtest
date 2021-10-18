from collections import defaultdict, deque
n = int(input())
c = int(input())
graph = defaultdict(list)
check = [False] * (n + 1)

for _ in range(c):
	a, b = map(int, input().split())
	graph[a].append(b)
	graph[b].append(a)

q = deque([1])
ans = 0
check[1] = True

while q:
	now = q.popleft()
	for nex in graph[now]:
		if not check[nex]:
			check[nex] = True
			q.append(nex)
			ans += 1

print(ans)
