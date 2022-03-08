import sys
from itertools import product
N, M = map(int, sys.stdin.readline().rstrip().split())
nums = sorted(list(map(int, sys.stdin.readline().rstrip().split())))

res = list(product(nums, repeat=M))

for i in res:
    print(*i)


'''
def perm(res, n):
    if n == M:
        print(*res)

    for i in range(N):
        if visited[i] < M:
            res.append(nums[i])
            visited[i] += 1
            perm(res, n+1)
            res.pop()
            visited[i] -= 1

import sys
N, M = map(int, sys.stdin.readline().rstrip().split())
nums = sorted(list(map(int, sys.stdin.readline().rstrip().split())))

visited = [0] * N
res = []

perm(res, 0)
'''