import sys

N, K = map(int, sys.stdin.readline().split())

if K == 0:
    print(1)

else:
    up = 1
    down = 1

    for i in range(1, N+1):
        up *= i

    for j in range(1, N-K+1):
        down *= j

    for k in range(1, K+1):
        down *= k

    print(up // down)