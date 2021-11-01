'''
정수를 저장한 배열, arr 에서 가장 작은 수를 제거한 배열을 리턴하는 함수, solution을 완성해주세요.
단, 리턴하려는 배열이 빈 배열인 경우엔 배열에 -1을 채워 리턴하세요.

arr은 길이 1 이상인 배열입니다.
인덱스 i, j에 대해 i ≠ j이면 arr[i] ≠ arr[j] 입니다.
'''

def solution(arr):
    arr.remove(min(arr))

    if len(arr):
        return arr

    else:
        return [-1]

print(solution([4,3,2,1]))    # [4,3,2]
print(solution([10]))    # [-1]
