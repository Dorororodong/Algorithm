dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def bfs(x, y):
    width = 1
    q = deque()
    q.append((x, y))

    while q:
        x, y = q.popleft()

        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]

            if 0 <= nx < M and 0 <= ny < N:
                if grid[nx][ny] == 0:
                    grid[nx][ny] = 1
                    q.append((nx, ny))
                    width += 1

    res.append(width)

import sys
from collections import deque
M, N, K = map(int, sys.stdin.readline().rstrip().split())

grid = [[0] * N for _ in range(M)]

res = []

for _ in range(K):
    x, y, a, b = map(int, sys.stdin.readline().rstrip().split())

    for i in range(M - b, M - y):
        for j in range(x, a):
            grid[i][j] = 1

for i in range(M):
    for j in range(N):
        if grid[i][j] == 0:
            grid[i][j] = 1
            bfs(i, j)

res.sort()

print(len(res))
print(" ".join(map(str, res)))