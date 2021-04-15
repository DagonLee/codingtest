d = [[0] * 2 for _ in range(91)]
d[1][1] = 1
for i in range(2, 91):
	d[i][0] = d[i - 1][0] + d[i - 1][1]
	d[i][1] = d[i - 1][0]
n = int(input())
print(sum(d[n]))
