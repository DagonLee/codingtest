from collections import deque
n = int(input())
m = [list(map(int, input().split())) for _ in range(n)]

q = deque()
t = 0 #시간
s = 2 #크기
e = 0 #먹은 물고기 수

dx = [-1, 0, 0, 1]
dy = [0, -1, 1, 0]
while True:
	for z in range(n * n):
		i = z // n
		j = z % n
		if m[i][j] == 9:
			q.append((i, j))
			fish = []
			d = [[-1] * n for _ in range(n)]
			d[i][j] = 0
			while q:
				x, y = q.popleft()
				for k in range(4):
					nx, ny = x + dx[k], y + dy[k]
					if nx < 0 or n <= nx or ny < 0 or n <= ny:
						continue
					if m[nx][ny] <= s and d[nx][ny] == -1:
						d[nx][ny] = d[x][y] + 1
						q.append((nx, ny))
						if 0 < m[nx][ny] < s:
							fish.append((d[nx][ny], nx, ny))
			fish.sort()
			if fish:
				m[i][j] = 0
				e += 1
				t += fish[0][0]
				if s == e:
					s += 1
					e = 0
				m[fish[0][1]][fish[0][2]] = 9
				break
			else:
				print(t)
				exit()
print(t)