import sys
from collections import deque
sys.stdin = open('input.txt')

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def BFS(x, y):
    Q = deque()
    Q.append((x, y))
    visited[x][y] = 1

    while Q:
        x, y = Q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < N and 0 <= ny < M and cabbage[nx][ny] == 1 and visited[nx][ny] == 0:
                visited[nx][ny] = 1
                Q.append((nx, ny))

T = int(input())

for tc in range(1, T+1):
    M, N, K = map(int, sys.stdin.readline().rstrip().split())     # 가로, 세로, 배추 심어져있는 개수
    cabbage = [[0] * M for _ in range(N)]
    visited = [[0] * M for _ in range(N)]

    for _ in range(K):
        X, Y = map(int, sys.stdin.readline().rstrip().split())
        cabbage[Y][X] = 1

    cnt = 0
    for i in range(N):
        for j in range(M):
            if cabbage[i][j] == 1 and visited[i][j] == 0:
                cnt += 1
                BFS(i, j)

    print(cnt)