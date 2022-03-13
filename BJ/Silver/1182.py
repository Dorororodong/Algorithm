# 있는 그대로 너무 돌아가는 방법
import sys
from itertools import combinations
N, S = map(int, sys.stdin.readline().rstrip().split())
nums = list(map(int, sys.stdin.readline().rstrip().split()))

res = []
cnt = 0

for i in range(1, N + 1):
    res.append(list(combinations(nums, i)))

for j in res:
    for k in j:
        if sum(k) == S:
            cnt += 1

print(cnt)

'''
# 어렵지 않게 바로 해결하는 방법
import sys
from itertools import combinations

input = sys.stdin.readline
n, s = map(int, input().split())
arr = list(map(int, input().split()))
cnt = 0
for i in range(1, n+1):
    comb = combinations(arr, i)

    for x in comb:
        if sum(x) == s:
            cnt += 1

print(cnt)
'''

'''
# 백트래킹!(+ 재귀) [하고싶었던 방법인데... 실패...]
import sys
input = sys.stdin.readline
n, s = map(int, input().split())
arr = list(map(int, input().split()))
cnt = 0

def subset_sum(idx, sub_sum):
    global cnt

    if idx >= n:
        return

    sub_sum += arr[idx]

    if sub_sum == s:
        cnt += 1
    
    # 현재 arr[idx]를 선택한 경우의 가지
    subset_sum(idx+1, sub_sum)

    # 현재 arr[idx]를 선택하지 않은 경우의 가지
    subset_sum(idx+1, sub_sum - arr[idx])

subset_sum(0, 0)
print(cnt)
'''