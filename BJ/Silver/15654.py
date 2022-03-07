# 순열... permutations

def sequence(res, cnt):
    if cnt == M:
        print(*res)

    else:
        for i in range(len(nums)):
            if visited[i] == 0:
                res.append(nums[i])
                visited[i] = 1
                sequence(res, cnt + 1)
                res.pop()
                visited[i] = 0

import sys
N, M = map(int, sys.stdin.readline().rstrip().split())
nums = list(map(int, sys.stdin.readline().rstrip().split()))
visited = [0] * N
nums.sort()

res = []

sequence(res, 0)

'''
import sys
from itertools import permutations
n,m=map(int,input().split())
arr=sorted(list(map(int,input().split())))
print('\n'.join(map(' '.join,permutations(map(str,arr),m))))
'''