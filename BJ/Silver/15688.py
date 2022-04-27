import sys
N = int(sys.stdin.readline().rstrip())
K = [int(sys.stdin.readline().rstrip()) for _ in range(N)]

K.sort()

for i in K:
    print(i)