import sys
sys.stdin = open('input.txt')

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def DFS(x, y):
    cabbage[x][y] = 2

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < N and 0 <= ny < M and cabbage[nx][ny] == 1:
            DFS(nx, ny)

T = int(input())

for tc in range(1, T+1):
    M, N, K = map(int, input().split())
    cabbage = [[0] * M for _ in range(N)]
    visited = [[0] * M for _ in range(N)]

    for _ in range(K):
        X, Y = map(int, input().split())
        cabbage[Y][X] = 1
        visited[Y][X] = 1

    cnt = 0
    for i in range(N):
        for j in range(M):
            if cabbage[i][j] == 1:
                cnt += 1
                DFS(i, j)

    print(cnt)