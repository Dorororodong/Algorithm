import sys
sys.stdin = open('input.txt')

T = int(input())
dp = [0] * 101
dp[1] = 1
dp[2] = 1
dp[3] = 1

for _ in range(T):
    N = int(input())
    if N < 4:
        print(dp[N])
    for i in range(1, N-2):
        dp[i+3] = dp[i] + dp[i+1]
    print(dp[N])