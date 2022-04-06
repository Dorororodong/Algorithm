dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def BFS(x, y, n):
    visited[x][y] = 1
    Q = deque()
    Q.append((x, y, n))

    while Q:
        x, y, n = Q.popleft()

        live[n] += 1
        live[n + flower[x][y]] -= 1             # 언제 꽃이 지는가?

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < N and 0 <= ny < M:
                if visited[nx][ny] == 0:
                    if flower[nx][ny] != 0:     # 0이면 꽃이 피지 않음
                        visited[nx][ny] = 1
                        Q.append((nx, ny, n + 1))

import sys
from collections import deque
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().rstrip().split())
    flower = [list(map(int, input().rstrip().split())) for _ in range(N)]
    visited = [[0] * M for _ in range(N)]
    sx, sy = map(int, input().rstrip().split())
    live = [0] * 1250001                            # 밭의 크기와 땅의 비옥함

    BFS(sx, sy, 1)

    max_day = -1
    max_cnt = -1
    cnt = 0

    for day in range(1, 1250001):
        cnt += live[day]
        if max_cnt < cnt:           # 끝까지 가면서 중간중간 증가하면 최대 변경
            max_cnt = cnt
            max_day = day           # 그 날도 갱신

    print('#{} {}일 {}개'.format(tc, max_day, max_cnt))

#1 2일 3개
#2 5일 7개