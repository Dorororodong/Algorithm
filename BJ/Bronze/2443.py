import sys
N = int(sys.stdin.readline().rstrip())

for i in range(N, 0, -1):
    print(' ' * (N - i) + '*' * (2 * i - 1))