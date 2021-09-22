'''
array의 길이는 1 이상 100 이하입니다.
array의 각 원소는 1 이상 100 이하입니다.
commands의 길이는 1 이상 50 이하입니다.
commands의 각 원소는 길이가 3입니다.
'''
def solution(array, commands):
    answer = []

    for i in range(len(commands)):                              # 리스트 초기화 때문에, 범위로 지정
        array = array                                           # 리스트는 바뀌니까 늘 초기화 필요
        target_array = array[commands[i][0]-1:commands[i][1]]   # 시작, 끝 주고
        target_array = sorted(target_array)                     # 정렬 한번 하고
        answer.append(target_array[commands[i][2]-1])           # 해당 숫자만 삽입

    return answer

print(solution([1, 5, 2, 6, 3, 7, 4], [[2, 5, 3], [4, 4, 1], [1, 7, 3]]))
# [5, 6, 3]


'''
# array를 건드리지 않고...
def solution(array, commands):
    answer = []
    for command in commands:
        i,j,k = command
        answer.append(list(sorted(array[i-1:j]))[k-1])
    return answer


# lambda...!?
def solution(array, commands):
    return list(map(lambda x:sorted(array[x[0]-1:x[1]])[x[2]-1], commands))    
'''

