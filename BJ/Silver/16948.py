dx = [-2, -2, 0, 0, 2, 2]
dy = [-1, 1, -2, 2, -1, 1]

def bfs(x, y, n):
    global min_cnt

    q = deque()
    q.append((x, y, n))
    arr[x][y] = 1

    while q:
        x, y, n = q.popleft()

        if x == r2 and y == c2:
            if min_cnt > n:
                min_cnt = n

        for i in range(6):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < N and 0 <= ny < N:
                if arr[nx][ny] == 0:
                    arr[nx][ny] = 1
                    q.append((nx, ny, n + 1))

import sys
from collections import deque
N = int(sys.stdin.readline().rstrip())
r1, c1, r2, c2 = map(int, sys.stdin.readline().rstrip().split())

arr = [[0] * N for _ in range(N)]
min_cnt = 987654321

bfs(r1, c1, 0)

if min_cnt == 987654321:
    print(-1)

else:
    print(min_cnt)