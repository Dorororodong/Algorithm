from collections import deque

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def BFS(x, y):
    global cnt

    Q = deque()
    Q.append((x, y))
    map_list[x][y] = 'T'

    while Q:
        x, y = Q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < N and 0 <= ny < N and map_list[nx][ny] == 1:
                map_list[nx][ny] = 'T'
                cnt += 1
                Q.append((nx, ny))

    result.append(cnt)
    return

N = int(input())

map_list = [list(map(int, input())) for _ in range(N)]
# print(map_list)

result = []
for i in range(N):
    for j in range(N):
        if map_list[i][j] == 1:
            cnt = 1
            BFS(i, j)

result.sort()
print(len(result))
for i in result:
    print(i)