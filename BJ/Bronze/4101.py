import sys
while True:
    a, b = map(int, sys.stdin.readline().rstrip().split())
    if a == 0:
        break

    else:
        if a > b:
            print('Yes')

        else:
            print('No')