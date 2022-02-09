import sys
n = int(sys.stdin.readline().rstrip())
dp = [0, 1, 2]

if n < 3:
    print(dp[n])

else:
    for i in range(3, n + 1):
        dp.append(dp[i-1] + dp[i-2])

    print(dp[n] % 10007)