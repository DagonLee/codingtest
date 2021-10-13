n, m = map(int, input().split())
trees = list(map(int, input().split()))
left = 0
right = max(trees)

while left <= right:
    mid = (left + right) // 2
    cutted = 0
    for tree in trees:
        if tree - mid > 0:
            cutted += (tree - mid)
    if cutted >= m:
        left = mid + 1
    else:
        right = mid - 1

print(right)
