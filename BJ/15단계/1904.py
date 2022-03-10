import sys
N = int(sys.stdin.readline().rstrip())
dp = [0] * 1000001
dp[1] = 1
dp[2] = 2

for i in range(3, N + 1):
    dp[i] = dp[i - 1] + dp[i - 2]

print(dp[N] % 15746)

'''
n = int(input())
MOD = 15746
x, y = 1, 1
for _ in range(n):
    x, y = y, (x + y) % MOD
print(x)
'''