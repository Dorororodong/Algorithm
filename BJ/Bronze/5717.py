import sys

while True:
    x, y = map(int, sys.stdin.readline().rstrip().split())
    if x == 0:
        break

    else:
        print(x + y)