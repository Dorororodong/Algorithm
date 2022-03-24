# bfs의 구조 : deque에 담겨서 하나씩 나아가는... (즉, 퍼져나간다는 것) [FIFO]
# 메모리 초과 : 적게 할 수 있는 행위를 많이 하고 있지는 않은지? (0을 담을게 아니라 1을 담는다면?!)

dx = [0 , 0, 1, -1]
dy = [1, -1, 0, 0]
def bfs():
    while q:
        x, y, ox, oy = q.popleft()

        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]

            if 0 <= nx < n and 0 <= ny < m:
                if bitmap[nx][ny] == 0:
                    if ans[nx][ny] == 0:
                        ans[nx][ny] = abs(nx - ox) + abs(ny - oy)
                        q.append((nx, ny, ox, oy))

                    else:
                        if ans[nx][ny] > abs(nx - ox) + abs(ny - oy):
                            ans[nx][ny] = abs(nx - ox) + abs(ny - oy)
                            q.append((nx, ny, ox, oy))

import sys
from collections import deque
n, m = map(int, sys.stdin.readline().rstrip().split())
bitmap = [list(map(int, sys.stdin.readline().rstrip())) for _ in range(n)]

ans = [[0] * m for _ in range(n)]
q = deque()

for i in range(n):
    for j in range(m):
        if bitmap[i][j] == 1:
            q.append((i, j, i, j))
bfs()

for i in ans:
    print(' '.join(map(str, i)))