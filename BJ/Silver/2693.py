import sys
T = int(sys.stdin.readline().rstrip())

for _ in range(T):
    A = list(map(int, sys.stdin.readline().rstrip().split()))
    print(sorted(A)[-3])