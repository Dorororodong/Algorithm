import sys
N = int(sys.stdin.readline().rstrip())
seq = list(map(int, sys.stdin.readline().rstrip().split()))
dp = [1] * N

for i in range(N):
    for j in range(i):
        if seq[i] > seq[j]:
            dp[i] = max(dp[i], dp[j]+1)

print(max(dp))