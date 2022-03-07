def sequence(res, cnt):
    if cnt == M:
        print(*res)

    else:
        for i in range(len(nums)):
            if visited[i] != M:
                if len(res) > 0:
                    if res[-1] <= nums[i]:
                        res.append(nums[i])
                        visited[i] += 1
                        sequence(res, cnt + 1)
                        res.pop()
                        visited[i] -= 1

                else:
                    res.append(nums[i])
                    visited[i] += 1
                    sequence(res, cnt + 1)
                    res.pop()
                    visited[i] -= 1

import sys
N, M = map(int, sys.stdin.readline().rstrip().split())
nums = list(map(int, sys.stdin.readline().rstrip().split()))
visited = [0] * N
nums.sort()

res = []

sequence(res, 0)