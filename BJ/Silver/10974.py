def perm(cnt):
    if cnt == N:
        print(' '.join(map(str, res)))
        return

    for i in range(N):
        if visited[i] == 0:
            visited[i] = 1
            res.append(arr[i])
            perm(cnt + 1)
            visited[i] = 0
            res.pop()

import sys
N = int(sys.stdin.readline().rstrip())
arr = [i for i in range(1, N+1)]
visited = [0] * N
res = []

perm(0)