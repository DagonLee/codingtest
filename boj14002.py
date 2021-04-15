n = int(input())
a = list(map(int, input().split()))
d = [0] * n
v = [-1] * n
for i in range(n):
	d[i] = 1
	for j in range(i):
		if a[j] < a[i] and d[i] < d[j] + 1:
			d[i] = d[j] + 1
			v[i] = j
ans = 0
idx = 0
seq_lst = []
for i, k in enumerate(d):
	if k > ans:
		ans = k
		idx = i
while idx != -1:
	seq_lst.append(a[idx])
	idx = v[idx]
seq_lst = seq_lst[::-1]
print(ans)
print(' '.join(map(str, seq_lst)))