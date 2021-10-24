import sys
sys.stdin = open('input.txt')

'''
from collections import deque

dx = [0, 1]     # 우하
dy = [1, 0]

def BFS(x, y):
    global result

    Q = deque()
    Q.append((x, y))
    visited[x][y] = 1

    while Q:
        x, y = Q.popleft()

        if hopscotch[x][y] == 0:
            result = "YES"
            return

        for i in range(2):
            nx = x + dx[i] * hopscotch[x][y]
            ny = y + dy[i] * hopscotch[x][y]

            if 0 <= nx < N and 0 <= ny < N and visited[nx][ny] == 0:
                Q.append((nx, ny))

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    hopscotch = [list(map(int, input().split())) for _ in range(N)]
    visited = [[0] * N for _ in range(N)]
    # print(hopscotch)
    result = "NO"

    BFS(0, 0)

    print(result)

# YES
# NO
'''


dx = [0, 1]     # 우하
dy = [1, 0]

def DFS(x, y):
    global result

    visited[x][y] = 1

    if hopscotch[x][y] == 0:
        result = "YES"
        return

    for i in range(2):
        nx = x + dx[i] * hopscotch[x][y]
        ny = y + dy[i] * hopscotch[x][y]

        if 0 <= nx < N and 0 <= ny < N and visited[nx][ny] == 0:
            DFS(nx, ny)

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    hopscotch = [list(map(int, input().split())) for _ in range(N)]
    visited = [[0] * N for _ in range(N)]
    # print(hopscotch)
    result = "NO"

    DFS(0, 0)

    print(result)

# YES
# NO