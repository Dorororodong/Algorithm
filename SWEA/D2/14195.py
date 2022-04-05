dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def BFS(x, y):
    global max_size
    cnt = 1
    q = deque()
    q.append((x, y))

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < N and 0 <= ny < M:
                if visited[nx][ny] == 0:
                    if soil[nx][ny] == soil[x][y]:
                        visited[nx][ny] = 1
                        cnt += 1
                        q.append((nx, ny))

    if max_size < cnt:
        max_size = cnt

import sys
from collections import deque
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().rstrip().split())
    soil = [list(input()) for _ in range(N)]
    visited = [[0] * M for _ in range(N)]
    # print(soil)
    # print(visited)
    max_size = -1
    cnt_A = 0
    cnt_B = 0

    for i in range(N):
        for j in range(M):
            if soil[i][j] == 'A' and visited[i][j] == 0:
                visited[i][j] = 1
                cnt_A += 1
                BFS(i, j)

            elif soil[i][j] == 'B' and visited[i][j] == 0:
                visited[i][j] = 1
                cnt_B += 1
                BFS(i, j)

    print('#{} {} {} {}'.format(tc, cnt_A, cnt_B, max_size))

#1 2 3 4
#2 9 6 7