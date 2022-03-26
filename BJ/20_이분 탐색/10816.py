# print(nums_cnt) : Counter({10: 3, 3: 2, -10: 2, 6: 1, 2: 1, 7: 1})

import sys
from collections import Counter
N = int(sys.stdin.readline().rstrip())
nums = list(map(int, sys.stdin.readline().rstrip().split()))
M = int(sys.stdin.readline().rstrip())
how_many = list(map(int, sys.stdin.readline().rstrip().split()))

nums_cnt = Counter(nums)

for i in how_many:
    print(nums_cnt[i], end=' ')