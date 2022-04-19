dx = [-2, -1, -2, -1, 2, 1, 2, 1]
dy = [-1, -2, 1, 2, -1, -2, 1, 2]

def BFS(x, y):
    global min_result

    Q = deque()
    Q.append((x, y))

    while Q:
        x, y = Q.popleft()

        if x == end[0] and y == end[1]:
            print(chess[x][y])
            break

        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < I and 0 <= ny < I and chess[nx][ny] == 0:
                chess[nx][ny] = chess[x][y] + 1
                Q.append((nx, ny))

import sys
from collections import deque
T = int(sys.stdin.readline().rstrip())

for _ in range(1, T+1):
    I = int(sys.stdin.readline().rstrip())
    chess = [[0] * I for _ in range(I)]
    start = list(map(int, sys.stdin.readline().rstrip().split()))
    end = list(map(int, sys.stdin.readline().rstrip().split()))
    BFS(start[0], start[1])

'''
dx = [-2, -1, -2, -1, 2, 1, 2, 1]
dy = [-1, -2, 1, 2, -1, -2, 1, 2]

def BFS(x, y, t):
    global min_result

    Q = deque()
    Q.append((x, y, t))

    while Q:
        x, y, t = Q.popleft()

        if x == end[0] and y == end[1]:
            if min_result > t:
                min_result = t
                return

        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < I and 0 <= ny < I and visited[nx][ny] == 0:
                visited[nx][ny] = 1
                Q.append((nx, ny, t+1))

import sys
from collections import deque
T = int(sys.stdin.readline().rstrip())

for _ in range(1, T+1):
    I = int(sys.stdin.readline().rstrip())
    chess = [[0] * I for _ in range(I)]
    visited = [[0] * I for _ in range(I)]
    start = list(map(int, sys.stdin.readline().rstrip().split()))
    end = list(map(int, sys.stdin.readline().rstrip().split()))
    min_result = 987654321
    cnt = 0

    BFS(start[0], start[1], cnt)
    print(min_result)
'''