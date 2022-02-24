# 토마토와 비슷하다! 동시에 퍼져나가는 느낌으로 보면 되니까 안전거리가! [적은 쪽에서 항상 생각해보자, 그래야 시간단축!]
dx = [-1, -1, -1, 0, 0, 1, 1, 1]
dy = [-1, 0, 1, -1, 1, -1, 0, 1]

def BFS():
    global safety_dis
    while Q:
        x, y = Q.popleft()

        for j in range(8):
            nx = x + dx[j]
            ny = y + dy[j]

            if 0 <= nx < N and 0 <= ny < M:
                if shark[nx][ny] == 0:
                    shark[nx][ny] = shark[x][y] + 1
                    Q.append((nx, ny))

import sys
from collections import deque
N, M = map(int, sys.stdin.readline().rstrip().split())
shark = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(N)]
Q = deque([])
safety_dis = -1

for i in range(N):
    for j in range(M):
        if shark[i][j] == 1:
            Q.append((i, j))

BFS()

for k in shark:
    if max(k) > safety_dis:
        safety_dis = max(k)

print(safety_dis - 1)