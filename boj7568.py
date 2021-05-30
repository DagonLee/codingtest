n = int(input())
v = []
for _ in range(n):
	v.append(list(map(int, input().split())))
rank = [1] * len(v)
for i in range(len(v)):
	for j in range(i + 1, len(v)):
		if v[i][0] > v[j][0] and v[i][1] > v[j][1]:
			rank[j] += 1
		elif v[j][0] > v[i][0] and v[j][1] > v[i][1]:
			rank[i] += 1

for i in rank:
	print(i, end=' ')
