'''
피보나치 수는 F(0) = 0, F(1) = 1일 때, 1 이상의 n에 대하여 F(n) = F(n-1) + F(n-2) 가 적용되는 수 입니다.
2 이상의 n이 입력되었을 때, n번째 피보나치 수를 1234567으로 나눈 나머지를 리턴하는 함수, solution을 완성해 주세요.

n은 2 이상 100,000 이하인 자연수입니다.
'''

def solution(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        dp = [0] * (n + 1)
        dp[1] = 1
        for i in range(2, n+1):
            dp[i] = dp[i-1] + dp[i-2]
        return dp[n] % 1234567

# def solution(n):
#     a, b = 0, 1
#     for i in range(n):
#         a, b = b, a + b
#     return a % 1234567

print(solution(3))      # 2
print(solution(5))      # 5