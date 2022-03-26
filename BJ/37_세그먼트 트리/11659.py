# prefix_sum : 누적합!
import sys
N, M = map(int, sys.stdin.readline().rstrip().split())
nums = list(map(int, sys.stdin.readline().rstrip().split()))
prefix_sum = [0]

temp = 0
for i in range(N):
    temp += nums[i]
    prefix_sum.append(temp)

for _ in range(M):
    i, j = map(int, sys.stdin.readline().rstrip().split())
    print(prefix_sum[j] - prefix_sum[i-1])

'''
안되는 풀이...?...?...
import sys
N, M = map(int, sys.stdin.readline().rstrip().split())
nums = list(map(int, sys.stdin.readline().rstrip().split()))

for i in range(N-1, 0, -1):
    nums[i] = sum(nums[:i+1])

nums = [0] + nums
for _ in range(M):
    i, j = map(int, sys.stdin.readline().rstrip().split())
    print(nums[j] - nums[i-1])
'''