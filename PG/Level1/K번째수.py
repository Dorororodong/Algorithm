def solution(array, commands):
    result = []

    for i in commands:
        num = array[i[0] -1 : i[1]]
        num.sort()
        result.append(num[i[2] - 1])

    return result

print(solution([1, 5, 2, 6, 3, 7, 4], [[2, 5, 3], [4, 4, 1], [1, 7, 3]]))
