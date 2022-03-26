# 입력을 잘보자! 방심 ㄴㄴ
N = int(input())

if N == 0:
    print(0)

else:
    dp = [0] * (N+1)
    dp[1] = 1
    k = N-1

    while k > 0:
        for i in range(N-1, -1, -1):
            if dp[i] > 0:
                dp[i+1] = dp[i] + dp[i-1]
                k -= 1
                break
    print(dp[N])


'''
N = int(input())

def fibo(n):
    if n == 1:
        return 1
    elif n == 0:
        return 0
    else:
        return fibo(n-1) + fibo(n-2)

print(fibo(N))
'''

'''
def fibo(n):
    if n <= 1: return n
    return fibo(n-1) + fibo(n-2)

print(fibo(int(input())))
'''