import sys

for _ in range(3):
    N = int(sys.stdin.readline().rstrip())
    S = 0

    for _ in range(N):
        S += int(sys.stdin.readline().rstrip())

    if S == 0:
        print(0)

    elif S > 0:
        print('+')

    else:
        print('-')