import sys
n = int(sys.stdin.readline().rstrip())

for _ in range(n):
    X, Y = map(int, sys.stdin.readline().rstrip().split())

    if X >= Y:
        print('MMM BRAINS')

    else:
        print('NO BRAINS')