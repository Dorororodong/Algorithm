# 수학, 백트래킹, 재귀
def DFS(nums, cnt):
    if cnt == 0:
        if result == sorted(result):
            print(*result)

    for i in range(6-cnt, k):
        if visited[i] == 0:
            visited[i] = 1
            result.append(nums[i])
            DFS(nums, cnt-1)
            visited[i] = 0
            result.pop()

import sys
while True:
    nums_with_k = list(map(int, sys.stdin.readline().rstrip().split()))
    if len(nums_with_k) == 1:
        break

    else:
        result = []
        k = nums_with_k[0]
        nums = nums_with_k[1:]
        visited = [0] * k

        DFS(nums, 6)
        print()

'''
# 수학, 조합론
import sys
from itertools import combinations

while True:
    l = list(map(int, sys.stdin.readline().rstrip().split()))
    k = l[0]
    if k == 0:
        break
    S = l[1:]

    for i in combinations(S, 6):
        print(" ".join(map(str, i)))

    print()
'''