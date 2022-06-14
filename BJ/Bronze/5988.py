import sys
N = int(sys.stdin.readline().rstrip())

for _ in range(N):
    word = int(sys.stdin.readline().rstrip())

    if word % 2:
        print('odd')

    else:
        print('even')