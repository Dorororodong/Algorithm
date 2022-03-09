def perm(res, n):
    if n == M:
        print(' '.join(map(str, res)))
        return

    now = 0
    for i in range(N):
        if len(res) > 0:
            if res[-1] <= nums[i]:
                if nums[i] != now:
                    if visited[i] < M:
                        now = nums[i]
                        res.append(nums[i])
                        visited[i] += 1
                        perm(res, n+1)
                        res.pop()
                        visited[i] -= 1

        else:
            if nums[i] != now:
                now = nums[i]
                res.append(nums[i])
                visited[i] += 1
                perm(res, n + 1)
                res.pop()
                visited[i] -= 1

import sys
N, M = map(int, sys.stdin.readline().rstrip().split())
nums = sorted(list(map(int, sys.stdin.readline().rstrip().split())))

visited = [0] * N
res = []

perm(res, 0)