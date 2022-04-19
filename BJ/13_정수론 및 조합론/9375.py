# try/except도 가능!

import sys
from collections import defaultdict
T = int(sys.stdin.readline().rstrip())

for _ in range(T):
    n = int(sys.stdin.readline().rstrip())
    fassion = defaultdict(int)
    res = 1

    for _ in range(n):
        a, b = sys.stdin.readline().rstrip().split()
        fassion[b] += 1

    items = dict(fassion).values()

    for i in items:
        res *= (i + 1)

    print(res - 1)