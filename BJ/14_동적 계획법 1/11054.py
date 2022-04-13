import sys
N = int(sys.stdin.readline().rstrip())
A = list(map(int, sys.stdin.readline().rstrip().split()))

dp_increase = [1] * N
dp_decrease = [1] * N
dp_res = []

for i in range(N):
    for j in range(i):
        if A[i] > A[j]:
            dp_increase[i] = max(dp_increase[j] + 1, dp_increase[i])

for i in range(N-1, -1, -1):
    for j in range(N-1, i-1, -1):
        if A[i] > A[j]:
            dp_decrease[i] = max(dp_decrease[j] + 1, dp_decrease[i])

for i in range(N):
    dp_res.append(dp_increase[i] + dp_decrease[i] - 1)

print(max(dp_res))