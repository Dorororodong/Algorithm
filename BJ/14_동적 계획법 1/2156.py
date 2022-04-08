import sys
n = int(sys.stdin.readline().rstrip())
nums = [int(sys.stdin.readline().rstrip()) for _ in range(n)]
dp = [0] * n
dp[0] = nums[0]

if n <= 1:
    print(dp[0])

elif n <= 2:
    dp[1] = dp[0] + nums[1]

    print(dp[1])

elif n <= 3:
    dp[1] = dp[0] + nums[1]
    dp[2] = max(dp[1], dp[0] + nums[2], nums[1] + nums[2])
    print(dp[2])

else:
    dp[1] = dp[0] + nums[1]
    dp[2] = max(dp[1], dp[0] + nums[2], nums[1] + nums[2])

    for i in range(3, n):
        dp[i] = max(dp[i-1], dp[i-3] + nums[i-1] + nums[i], dp[i-2] + nums[i])

    print(dp[-1])