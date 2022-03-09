def perm(res, n):
    if n == M:
        print(*res)

    now = 0
    for i in range(N):
        if visited[i] == 0:
            if nums[i] != now:
                if len(res) > 0:
                    if res[-1] <= nums[i]:
                        now = nums[i]
                        res.append(nums[i])
                        visited[i] = 1
                        perm(res, n+1)
                        res.pop()
                        visited[i] = 0

                else:
                    now = nums[i]
                    res.append(nums[i])
                    visited[i] = 1
                    perm(res, n + 1)
                    res.pop()
                    visited[i] = 0

import sys
N, M = map(int, sys.stdin.readline().rstrip().split())
nums = sorted(list(map(int, sys.stdin.readline().rstrip().split())))

visited = [0] * N
res = []

perm(res, 0)