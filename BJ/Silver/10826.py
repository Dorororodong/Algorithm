import sys
n = int(sys.stdin.readline().rstrip())
if n == 0:
    print(0)

elif n == 1:
    print(1)

else:
    dp = [0] * (n + 1)
    dp[1] = 1
    for i in range(2, n+1):
        dp[i] = dp[i-1] + dp[i-2]

    print(dp[n])

'''
n = int(input())
a, b= 0, 1
for i in range(n):
    a, b = b, a+b
print(a)
'''