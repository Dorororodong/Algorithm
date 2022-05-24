import sys
N = int(sys.stdin.readline().rstrip())

for i in range(1, N+1):
    print(' ' * (N - i) + '*' * (2 * i - 1))

for i in range(N-1, 0, -1):
    print(' ' * (N - i) + '*' * (2 * i - 1))