dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def bfs(x, y):
    global max_width
    width = 1
    q = deque()
    q.append((x, y))

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < m:
                if dohwaji[nx][ny]:
                    dohwaji[nx][ny] = 0
                    width += 1
                    q.append((nx, ny))

    if width > max_width:
        max_width = width

import sys
from collections import deque
n, m = map(int, sys.stdin.readline().rstrip().split())
dohwaji = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(n)]

cnt = 0
max_width = 0

for i in range(n):
    for j in range(m):
        if dohwaji[i][j]:
            dohwaji[i][j] = 0
            cnt += 1
            bfs(i, j)

print(cnt)
print(max_width)