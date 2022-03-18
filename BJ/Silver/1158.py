import sys
from collections import deque
N, K = map(int, sys.stdin.readline().rstrip().split())

nums = deque(i for i in range(1, N + 1))

print('<', end='')

while nums:
    for _ in range(K - 1):
        nums.append(nums.popleft())

    if len(nums) > 1:
        print(nums.popleft(), end='')
        print(',', end=' ')

    else:
        print(nums.popleft(), end='')

print('>')