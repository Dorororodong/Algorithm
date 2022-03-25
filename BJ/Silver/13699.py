import sys
n = int(sys.stdin.readline().rstrip())
dp = [0] * (n+1)

if n < 2:
    print(1)

else:
    dp[0] = 1
    dp[1] = 1

    for i in range(2, n + 1):
        for j in range(0, i):
            dp[i] += dp[j] * dp[i-j-1]

    print(dp[n])