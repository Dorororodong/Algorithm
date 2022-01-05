'''
주어진 숫자 중 3개의 수를 더했을 때 소수가 되는 경우의 개수를 구하려고 합니다.
숫자들이 들어있는 배열 nums가 매개변수로 주어질 때,
nums에 있는 숫자들 중 서로 다른 3개를 골라 더했을 때 소수가 되는 경우의 개수를 return 하도록 solution 함수를 완성해주세요.

nums에 들어있는 숫자의 개수는 3개 이상 50개 이하입니다.
nums의 각 원소는 1 이상 1,000 이하의 자연수이며, 중복된 숫자가 들어있지 않습니다.
'''

import math
def is_prime_number(x):
    global cnt
    for i in range(2, int(math.sqrt(x)) + 1):
        if x % i == 0:
            return
    cnt += 1


cnt = 0
def solution(nums):
    for i in range(len(nums) - 2):
        for j in range(i+1, len(nums)-1):
            for k in range(j+1, len(nums)):
                is_prime_number(nums[i] + nums[j] + nums[k])

    return cnt

print(solution([1, 2, 3, 4]))       # 1
print(solution([1, 2, 7, 6, 4]))    # 4