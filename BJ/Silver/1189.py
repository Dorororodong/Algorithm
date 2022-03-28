dx = [-1, 0, 0, 1]
dy = [0, 1, -1, 0]
def go_to_home(x, y, n):
    global cnt
    if n == K:
        if x == 0 and y == C - 1:
            cnt += 1
            return
        return

    visited[x][y] = 1

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < R and 0 <= ny < C:
            if comebackhome[nx][ny] != 'T':
                if visited[nx][ny] == 0:
                    go_to_home(nx, ny, n + 1)
                    visited[nx][ny] = 0

import sys
R, C, K = map(int, sys.stdin.readline().rstrip().split())
comebackhome = [list(sys.stdin.readline().rstrip()) for _ in range(R)]
visited = [[0] * C for _ in range(R)]
cnt = 0

go_to_home(R - 1, 0, 1)

print(cnt)