from collections import deque
dx = [-1, 0, 0, 1]
dy = [0, -1, 1, 0]


def bfs(i, j, c, m, s, z):
  q = deque()
  q.append((i, j))
  while q:
    x, y = q.popleft()
    for k in range(4):
      nx, ny = x + dx[k], y + dy[k]
      if nx < 0 or n <= nx or ny < 0 or n <= ny:
        continue
      if s == 0:
        if c[nx][ny] == False and m[nx][ny] == z:
          c[nx][ny] = True
          q.append((nx, ny))
      else:
        if c[nx][ny] == False:
          if (m[nx][ny] == 'R' or m[nx][ny] == 'G') and (z == 'R' or z == 'G'):
            c[nx][ny] = True
            q.append((nx, ny))
          elif m[nx][ny] == z:
            c[nx][ny] = True
            q.append((nx, ny))


n = int(input())
norm_check = [[False] * n for _ in range(n)]
ill_check = [[False] * n for _ in range(n)]
norm_cnt = 0
ill_cnt = 0
m = [list(input()) for _ in range(n)]
for i in range(n):
  for j in range(n):
    if norm_check[i][j] == False:
      norm_check[i][j] = True
      norm_cnt += 1
      bfs(i, j, norm_check, m, 0, m[i][j])
    if ill_check[i][j] == False:
      ill_check[i][j] = True
      ill_cnt += 1
      bfs(i, j, ill_check, m, 1, m[i][j])


print(norm_cnt, ill_cnt)