import sys

N = int(sys.stdin.readline().rstrip())

dp = [0 for _ in range(N + 1)]

for i in range(2, N + 1):
    dp[i] = dp[i - 1] + 1

    if i % 2 == 0 and dp[i] > dp[i // 2] + 1:
        dp[i] = dp[i // 2] + 1

    if i % 3 == 0 and dp[i] > dp[i // 3] + 1:
        dp[i] = dp[i // 3] + 1

print(dp[N])

'''
import sys

N = int(sys.stdin.readline().rstrip())

dp = [0] * (N+1)
dp[N] = 1

for i in range(N, 1, -1):
    if dp[i] != 0:
        if i % 3 == 0:
            if i // 3 > 0:
                if dp[i // 3] == 0:
                    dp[i // 3] = dp[i] + 1

                else:
                    if dp[i // 3] > dp[i] + 1:
                        dp[i // 3] = dp[i] + 1

        if i % 2 == 0:
            if i // 2 > 0:
                if dp[i // 2] == 0:
                    dp[i // 2] = dp[i] + 1

                else:
                    if dp[i // 2] > dp[i] + 1:
                        dp[i // 2] = dp[i] + 1

        if dp[i-1] == 0:
            dp[i - 1] = dp[i] + 1

        else:
            if dp[i-1] > dp[i] + 1:
                dp[i - 1] = dp[i] + 1

print(dp[1] - 1)
'''