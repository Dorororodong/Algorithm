def below_sum(k, n):
    for _ in range(k):

    return below_sum()

import sys

T = int(sys.stdin.readline().rstrip())

for _ in range(1, T+1):
    k = int(sys.stdin.readline().rstrip())  # 층
    n = int(sys.stdin.readline().rstrip())  # 호

    zero = [i+1 for i in range(n)]
    below_sum(k, n)