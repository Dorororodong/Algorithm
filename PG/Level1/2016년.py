def solution(a, b):
    day = ['FRI', 'SAT', 'SUN', 'MON', 'TUE', 'WED', 'THU']
    month = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    cnt = 0

    for i in range(a - 1):
        cnt += month[i]

    return day[(cnt + b) % 7 - 1]

print(solution(5, 24))