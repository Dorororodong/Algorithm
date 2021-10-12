dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

from collections import deque

def BFS(x, y, n):
    global min_result

    Q = deque()
    Q.append((x, y, n))
    visited[x][y] = 1

    while Q:
        qx, qy, n = Q.popleft()

        if min_result < n:
            continue

        if qx == N - 1 and qy == M - 1:
            if min_result > n:
                min_result = n
                return

        for i in range(4):
            nx = qx + dx[i]
            ny = qy + dy[i]

            if 0 <= nx < N and 0 <= ny < M and visited[nx][ny] == 0 and maze[nx][ny] == 1:
                visited[nx][ny] = 1
                Q.append((nx, ny, n+1))


N, M = map(int, input().split())

maze = [list(map(int, input())) for _ in range(N)]
# print(maze)
visited = [[0] * M for _ in range(N)]

min_result = N * M + 1

BFS(0, 0, 1)

print(min_result)















'''
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def DFS(x, y, n):
    global min_result

    if min_result <= n:
        return

    if x == N - 1 and y == M - 1:
        if min_result > n:
            min_result = n
            return

    visited[x][y] = 1

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < N and 0 <= ny < M and visited[nx][ny] == 0 and maze[nx][ny] == 1:
            DFS(nx, ny, n+1)
            visited[nx][ny] = 0

N, M = map(int, input().split())

maze = [list(map(int, input())) for _ in range(N)]
# print(maze)
visited = [[0] * M for _ in range(N)]

min_result = N * M + 1

DFS(0, 0, 1)

print(min_result)
'''