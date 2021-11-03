'''
array의 각 element 중 divisor로 나누어 떨어지는 값을 오름차순으로 정렬한 배열을 반환하는 함수, solution을 작성해주세요.
divisor로 나누어 떨어지는 element가 하나도 없다면 배열에 -1을 담아 반환하세요.

arr은 자연수를 담은 배열입니다.
정수 i, j에 대해 i ≠ j 이면 arr[i] ≠ arr[j] 입니다.
divisor는 자연수입니다.
array는 길이 1 이상인 배열입니다.
'''

def solution(arr, divisor):
    result = []
    for i in range(len(arr)):
        if arr[i] % divisor == 0:
            result.append(arr[i])

    if len(result) == 0:
        return [-1]
    else:
        return sorted(result)

    # def solution(arr, divisor): return sorted([n for n in arr if n%divisor == 0]) or [-1]

print(solution([5, 9, 7, 10], 5))   # [5, 10]
print(solution([2, 36, 1, 3], 1))   # [1, 2, 3, 36]
print(solution([3,2,6], 10))        # [-1]
