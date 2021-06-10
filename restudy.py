n,s = map(int,input().split())
a = list(map(int,input().split()))
m = n//2
n = n-m
first = [0]*(1<<n)
for i in range(1<<n):
    for k in range(n):
        if (i&(1<<k)) > 0:
            first[i] += a[k]
second = [0]*(1<<m)
for i in range(1<<m):
    for k in range(m):
        if (i&(1<<k)) > 0:
            second[i] += a[k+n]
first.sort()
second.sort()
second.reverse()
print(first, second)