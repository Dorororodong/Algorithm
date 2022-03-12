import sys
N = int(sys.stdin.readline().rstrip())

for _ in range(N):
    r, e, c = map(int, sys.stdin.readline().rstrip().split())

    if r > e - c:
        print('do not advertise')

    elif r == e - c:
        print('does not matter')

    else:
        print('advertise')