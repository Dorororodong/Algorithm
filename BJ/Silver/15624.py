import sys
n = int(sys.stdin.readline().rstrip())
dp = [0] * (n+1)

if n >= 1:
    dp[1] = 1

    for i in range(2, n+1):
        dp[i] = (dp[i-1] + dp[i-2]) % 1000000007

    print(dp[n])

else:
    print(0)