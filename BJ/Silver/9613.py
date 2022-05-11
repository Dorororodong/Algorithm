import sys
import math
from itertools import combinations
t = int(sys.stdin.readline().rstrip())

for _ in range(t):
    nums = list(map(int, sys.stdin.readline().rstrip().split()))
    nums_n = nums[1:]

    comb = list(combinations(nums_n, 2))

    res = 0
    for i in comb:
        res += math.gcd(*i)

    print(res)