T = int(input())
for tc in range(1, T+1):
    N = int(input())
    dp = [0] * (N+1)
    if N == 0:
        print(1, 0)
    elif N == 1:
        print(0, 1)
    else:
        dp[N] = 1
        for i in range(N, 1, -1):
            dp[N-1] += 1
            dp[N-2] += 1
        print(dp[0], dp[1])


# def fibo(n):
#     global zero
#     global one
#
#     if n == 0:
#         zero += 1
#         return
#
#     elif n == 1:
#         one += 1
#         return
#
#     else:
#         fibo(n - 1)
#         fibo(n - 2)
#         return
#
# T = int(input())
#
# for tc in range(1, T+1):
#     zero = 0
#     one = 0
#     fibo(int(input()))
#     print(zero, one)