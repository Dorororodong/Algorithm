'''
피보나치 수열은 다음과 같이 그 전 두 항의 합으로 계산되는 수열이다. 첫 두 항은 1로 정의된다.

f(1) = 1, f(2) = 1, f(n > 2) = f(n − 1) + f(n − 2)

정수를 입력받아, 그에 해당하는 피보나치 수를 출력하는 프로그램을 작성하여라.
'''

import sys

N = int(sys.stdin.readline().rstrip())

if N == 1 or N == 2:
    print(1)

else:
    dp = [0] * (N+1)
    dp[1] = 1
    dp[2] = 1

    for i in range(3, N+1):
        if dp[i] == 0:
            dp[i] = dp[i-1] + dp[i-2]

    print(dp[N])
