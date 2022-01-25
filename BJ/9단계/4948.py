import sys
import math

while True:
    N = int(sys.stdin.readline().rstrip())
    cnt = [1] * (2 * N + 1)
    if N != 0:
        for i in range(2, int(math.sqrt(2 * N)) + 1):
            if cnt[i] == 1:
                for j in range(2 * i, 2 * N + 1, i):
                    cnt[j] = 0
        if N == 1:
            print(1)
        else:
            print(cnt[N+1:].count(1))
    else:
        break