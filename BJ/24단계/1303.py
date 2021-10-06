from collections import deque

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def BFS_W(x, y):
    cnt = 0
    Q = deque()
    visited[x][y] = 1
    Q.append((x, y))

    while Q:
        (x, y) = Q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < M and 0 <= ny < N and visited[nx][ny] == 0 and war[nx][ny] == 'W':
                    cnt += 1
                    visited[nx][ny] = 1
                    Q.append((nx, ny))

    white_list.append(cnt + 1)


def BFS_B(x, y):
    cnt = 0
    Q = deque()
    visited[x][y] = 1
    Q.append((x, y))

    while Q:
        (x, y) = Q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < M and 0 <= ny < N and visited[nx][ny] == 0 and war[nx][ny] == 'B':
                    cnt += 1
                    visited[nx][ny] = 1
                    Q.append((nx, ny))

    blue_list.append(cnt + 1)


N, M = map(int, input().split())
war = [list(map(str, input())) for _ in range(M)]
# print(war)

visited = [[0] * N for _ in range(M)]
# print(visited)

white_list = []
blue_list = []

for i in range(M):
    for j in range(N):
        if war[i][j] == 'W' and visited[i][j] == 0:
            BFS_W(i, j)

        elif war[i][j] == 'B' and visited[i][j] == 0:
            BFS_B(i, j)

result_W = 0
result_B = 0
for i in white_list:
    result_W += i ** 2

for j in blue_list:
    result_B += j ** 2

print(result_W, result_B)