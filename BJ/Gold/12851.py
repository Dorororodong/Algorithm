def BFS(n):
    Q = deque()
    Q.append((n))
    visited[n][0] = 0
    visited[n][1] = 1

    while Q:
        x = Q.popleft()

        for i in [x-1, x+1, 2*x]:
            if 0 <= i < 100001:
                if visited[i][0] == -1:                     # 처음 도달
                    visited[i][0] = visited[x][0] + 1       # 시간 + 1
                    visited[i][1] = visited[x][1]           # 경우의 수 그대로 감
                    Q.append((i))

                elif visited[i][0] == visited[x][0] + 1:    # 처음이 아니라면 (But 아직까진 최단)
                    visited[i][1] += visited[x][1]          # 경우의 수 갱신

import sys
from collections import deque
N, K = map(int, sys.stdin.readline().rstrip().split())

visited = [[-1, 0] for _ in range(100001)]        # 시간, 경우의 수

BFS(N)

print(visited[K][0])
print(visited[K][1])