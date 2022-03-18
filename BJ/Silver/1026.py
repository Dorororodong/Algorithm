import sys
N = int(sys.stdin.readline().rstrip())
A = list(map(int, sys.stdin.readline().rstrip().split()))
B = list(map(int, sys.stdin.readline().rstrip().split()))

A.sort(reverse=True)
B.sort()

res = 0

for i in range(N):
    res += A[i] * B[i]

print(res)