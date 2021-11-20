def recursion(n):
    if n == 0:
        return 1

    else:
        return n * recursion(n-1)

import sys

N = int(sys.stdin.readline())

print(recursion(N))