def gym_guy(w, n):
    global cnt

    if w < 500:
        return

    if n == N:
        cnt += 1
        return

    for i in range(N):
        if visited[i] == 0:
            visited[i] = 1
            gym_guy(w - K + A[i], n + 1)
            visited[i] = 0

import sys
N, K = map(int, sys.stdin.readline().rstrip().split())
A = list(map(int, sys.stdin.readline().rstrip().split()))
visited = [0] * N
cnt = 0
weight = 500

gym_guy(weight, 0)

print(cnt)