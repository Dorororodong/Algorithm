dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

from collections import deque

def BFS(x, y):
    global max_result
    global cnt

    Q = deque()
    Q.append((x, y))
    visited[x][y] = 1

    while Q:

        x, y = Q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < N and 0 <= ny < M and visited[nx][ny] == 0 and leftovers[nx][ny] == 1:
                cnt += 1
                visited[nx][ny] = 1
                Q.append((nx, ny))

    if max_result < cnt:
        max_result = cnt
        return

N, M, K = map(int, input().split())
leftovers = [[0] * M for _ in range(N)]
visited = [[0] * M for _ in range(N)]

for _ in range(K):
    y, x = map(int, input().split())
    leftovers[y-1][x-1] = 1

# print(leftovers)

max_result = 0

for i in range(N):
    for j in range(M):
        if leftovers[i][j] == 1 and visited[i][j] == 0:
            cnt = 1
            BFS(i, j)

print(max_result)
