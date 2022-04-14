dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

# bfs 돌기, 2가 퍼질 꺼니까 매번 복사해줘야함
def bfs():
    global max_res

    q = deque()
    copy_lab = copy.deepcopy(lab)
    for i in range(N):
        for j in range(M):
            if copy_lab[i][j] == 2:
                q.append((i, j))

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < N and 0 <= ny < M:
                if copy_lab[nx][ny] == 0:
                    copy_lab[nx][ny] = 2
                    q.append((nx, ny))

    res = 0
    for i in range(N):
        for j in range(M):
            if copy_lab[i][j] == 0:
                res += 1

    if max_res < res:
        max_res = res

# 벽 세우기
def wall(cnt):
    if cnt == 3:
        bfs()
        return

    for i in range(N):
        for j in range(M):
            if lab[i][j] == 0:
                lab[i][j] = 1
                wall(cnt + 1)
                lab[i][j] = 0

import sys
from collections import deque
import copy

N, M = map(int, sys.stdin.readline().rstrip().split())
lab = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(N)]

max_res = -1
wall(0)

print(max_res)