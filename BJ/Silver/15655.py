def perm(res, n):
    if n == M:
        print(*res)

    for i in range(N):
        if visited[i] == 0:
            if len(res) > 0:
                if res[-1] <= nums[i]:
                    res.append(nums[i])
                    visited[i] = 1
                    perm(res, n+1)
                    res.pop()
                    visited[i] = 0

            else:
                res.append(nums[i])
                visited[i] = 1
                perm(res, n+1)
                res.pop()
                visited[i] = 0

import sys
N, M = map(int, sys.stdin.readline().rstrip().split())
nums = sorted(list(map(int, sys.stdin.readline().rstrip().split())))

visited = [0] * N
res = []

perm(res, 0)