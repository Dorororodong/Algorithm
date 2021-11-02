import sys
sys.stdin = open('input.txt')

N = int(input())
dp = [0] * (N+1)


for i in range(1, N+1):
    number = list(map(int, input().split()))
    if len(number) == 1:
        dp[i] = number[0]
        idx = 0
    else:
        dp[i] = dp[i-1] + max(number[idx], number[idx+1])
        idx = number.index(max(number[idx], number[idx+1]))

print(dp[N])