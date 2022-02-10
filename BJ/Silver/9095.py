import sys
T = int(sys.stdin.readline().rstrip())

dp = [0, 1, 2, 4]
for i in range(4, 11):
    dp.append(dp[i - 1] + dp[i - 2] + dp[i - 3])

for _ in range(1, T + 1):
    n = int(sys.stdin.readline().rstrip())
    print(dp[n])