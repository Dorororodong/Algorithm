'''
정수 n을 입력받아 n의 약수를 모두 더한 값을 리턴하는 함수, solution을 완성해주세요.

n은 0 이상 3000이하인 정수입니다.
'''

def solution(n):
    result = 0
    for i in range(n, 0, -1):
        if n % i == 0:
            result += i
    return result

# def solution(num):
#     return num + sum([i for i in range(1, (num // 2) + 1) if num % i == 0])

# 2000이면, 1001부터는 계산이 의미가 없음, 나눠봤자 1도 안나오니까

print(solution(12))     # 28
print(solution(5))      # 6