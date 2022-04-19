# 범위로 지정하면 좋은 점 : 1개 2개 처럼 낮은 구간을 조건문으로 나누지 않아도 됨 (if N == 1... 이런거)

import sys
N = int(sys.stdin.readline().rstrip())
stairs = [0] * 300
dp = [0] * 300

for i in range(N):
    stairs[i] = int(sys.stdin.readline().rstrip())

dp[0] = stairs[0]
dp[1] = stairs[1] + stairs[0]
dp[2] = max(stairs[2] + stairs[0], stairs[2] + stairs[1])

for i in range(3, N):
    dp[i] = max(dp[i-2] + stairs[i], dp[i-3] + stairs[i-1] + stairs[i])

print(dp[N-1])