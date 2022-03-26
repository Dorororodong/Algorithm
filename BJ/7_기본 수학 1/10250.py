import sys

T = int(sys.stdin.readline().rstrip())

for _ in range(1, T+1):

    H, W, N = map(int, sys.stdin.readline().rstrip().split())

    if N % H == 0:
        print(H * 100 + (N // H))
    else:
        print((N % H) * 100 + (N // H + 1))