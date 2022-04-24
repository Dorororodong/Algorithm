import sys
N = int(sys.stdin.readline().rstrip())
A = list(map(int, sys.stdin.readline().rstrip().split()))

res = [N - 1] * N

for i in range(N - 1):
    for j in range(i + 1, N):
        if A[i] <= A[j]:
            res[i] -= 1

        else:
            res[j] -= 1

print(*res)