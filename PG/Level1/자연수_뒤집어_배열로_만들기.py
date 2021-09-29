'''
자연수 n을 뒤집어 각 자리 숫자를 원소로 가지는 배열 형태로 리턴해주세요. 예를들어 n이 12345이면 [5,4,3,2,1]을 리턴합니다.

n은 10,000,000,000이하인 자연수입니다.
'''


def solution(n):

    answer = list(map(int, str(n)))[::-1]
    # input이 str로 받으니까?!
    return answer

# def digit_reverse(n):
#     return list(map(int, reversed(str(n))))

print(solution(12345))
# [5,4,3,2,1]