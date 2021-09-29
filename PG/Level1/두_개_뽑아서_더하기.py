'''
정수 배열 numbers
numbers에서 서로 다른 인덱스에 있는 두 개의 수를 뽑아 더해서 만들 수 있는 모든 수를 배열에 오름차순으로 담아 return

numbers의 길이는 2 이상 100 이하입니다.
numbers의 모든 수는 0 이상 100 이하입니다.
'''


def solution(numbers):
    answer = []

    for i in range(len(numbers) - 1):
        for j in range(i+1, len(numbers)):
            if (numbers[i] + numbers[j]) not in answer:
                answer.append(numbers[i] + numbers[j])
    answer.sort()

    return answer

print(solution([2,1,3,4,1]))    # [2,3,4,5,6,7]
print(solution([5,0,2,7]))      # [2,5,7,9,12]


'''
from itertools import combinations

def solution(numbers):
    answer = []
    l = list(combinations(numbers, 2))

    for i in l:
        answer.append(sum(i))
    
    return sorted(list(set(answer)))
'''
