def solution(numbers):
    numbers = list(map(str, numbers))
    numbers.sort(key=lambda x: x * 3, reverse=True)
    ans = ''

    for i in numbers:
        ans += i

    if int(ans) != 0:
        return ans

    else:
        return '0'

print(solution([3, 30, 34, 5, 9]))