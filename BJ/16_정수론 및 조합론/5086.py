import sys

while True:
    N, M = map(int, sys.stdin.readline().rstrip().split())

    if N == 0:
        break

    else:
        if N % M == 0:
            print('multiple')

        elif M % N == 0:
            print('factor')

        else:
            print('neither')