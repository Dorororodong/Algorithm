import sys
n = int(sys.stdin.readline().rstrip())
dp = [0, 1]

if n < 2:
    print(n)

else:
    for i in range(2, n + 1):
        if i % 2:
            dp.append(dp[i - 1] * 2 - 1)
        else:
            dp.append(dp[i - 1] * 2 + 1)

    print(dp[n] % 10007)