dx = [-1, 1, 0, 0, 0, 0]
dy = [0, 0, 0, 0, 1, -1]
dz = [0, 0, 1, -1, 0, 0]
def BFS():
    global res
    while ripe:
        x, y, z = ripe.popleft()

        if tomato[x][y][z] > res:
            res = tomato[x][y][z]

        for i in range(6):
            nx = x + dx[i]
            ny = y + dy[i]
            nz = z + dz[i]

            if 0 <= nx < H and 0 <= ny < N and 0 <= nz < M:
                if tomato[nx][ny][nz] == 0:
                    tomato[nx][ny][nz] = tomato[x][y][z] + 1
                    ripe.append((nx, ny, nz))

import sys
from collections import deque
M, N, H = map(int, sys.stdin.readline().rstrip().split())
tomato = [[list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(N)] for _ in range(H)]
ripe = deque()
for i in range(H):                      # 높이
    for j in range(N):                  # 세로
        for k in range(M):              # 가로
            if tomato[i][j][k] == 1:
                ripe.append((i, j, k))

res = 0
BFS()
for i in tomato:
    for j in i:
        for k in j:
            if k == 0:
                print(-1)
                exit()
print(res - 1)