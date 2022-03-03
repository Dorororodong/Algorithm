# BFS, DFS 모두 가능
# 비색맹 먼저 해주고, 색맹 때는 색을 한 쪽으로 바꿔서 해줘도 괜찮겠네! ㅎ

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def cb_bfs(x, y):
    Q = deque()
    Q.append((x, y))

    while Q:
        x, y = Q.popleft()

        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]

            if 0 <= nx < N and  0 <= ny < N:
                if cb_visited[nx][ny] == 0:
                    if section[x][y] == 'B':
                        if section[nx][ny] == 'B':
                            cb_visited[nx][ny] = 1
                            Q.append((nx, ny))

                    else:
                        if section[nx][ny] != 'B':
                            cb_visited[nx][ny] = 1
                            Q.append((nx, ny))

def none_cb_bfs(x, y):
    W = deque()
    W.append((x, y))

    while W:
        x, y = W.popleft()

        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]

            if 0 <= nx < N and 0 <= ny < N:
                if none_cb_visited[nx][ny] == 0:
                    if section[x][y] == section[nx][ny]:
                            none_cb_visited[nx][ny] = 1
                            W.append((nx, ny))

import sys
from collections import deque
N = int(sys.stdin.readline().rstrip())

section = [list(sys.stdin.readline().rstrip()) for _ in range(N)]
cb_visited = [[0] * N for _ in range(N)]
none_cb_visited = [[0] * N for _ in range(N)]

cb_cnt = 0
none_cb_cnt = 0

for i in range(N):
    for j in range(N):
        if cb_visited[i][j] == 0:
            cb_visited[i][j] = 1
            cb_cnt += 1
            cb_bfs(i, j)

        if none_cb_visited[i][j] == 0:
            none_cb_visited[i][j] = 1
            none_cb_cnt += 1
            none_cb_bfs(i, j)

print(none_cb_cnt, cb_cnt)