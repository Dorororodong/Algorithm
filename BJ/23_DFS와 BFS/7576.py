# BFS 기본형에 너무 몰입... 결국 동시에 진행하는 경우가 있으니 Queue의 특성을 이용해서 선입선출...
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def BFS():
    global res
    while ripe:
        x, y = ripe.popleft()

        # 여기서 대소비교를 미리 해버리면?
        if tomato[x][y] > res:
            res = tomato[x][y]

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < N and 0 <= ny < M:
                if tomato[nx][ny] == 0:
                    tomato[nx][ny] = tomato[x][y] + 1
                    ripe.append((nx, ny))

import sys
from collections import deque

M, N = map(int, sys.stdin.readline().rstrip().split())
tomato = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(N)]
ripe = deque()
for i in range(N):
    for j in range(M):
        if tomato[i][j] == 1:
            ripe.append((i, j))

res = 0
BFS()
for i in tomato:
    for j in i:
        if j == 0:
            print(-1)
            exit()
print(res - 1)

'''
# 함수를 선언해서 안되는 경우 체크!
import sys
from collections import deque
_max = 0
M, N = map(int, sys.stdin.readline().split())
BOARD = [ list(map(int, sys.stdin.readline().split())) for _ in range(N) ]
queue = deque()
vectorX = [1, -1, 0, 0]
vectorY = [0, 0, 1, -1]

def checkBoard():
    for i in range(N):
        for j in range(M):
            if BOARD[i][j] == 0:
                return False
    return True

for i in range(N):
    for j in range(M):
        if BOARD[i][j] == 1:
            queue.append((i, j))

while queue:
    X, Y = queue.popleft()
    if BOARD[X][Y] > _max:
        _max = BOARD[X][Y]

    for i in range(4):
        dX, dY = X + vectorX[i], Y + vectorY[i]
        if 0 <= dX < N and 0 <= dY < M and BOARD[dX][dY] == 0:
            BOARD[dX][dY] = BOARD[X][Y] + 1
            queue.append((dX, dY))

print(_max-1 if checkBoard() else -1)
'''