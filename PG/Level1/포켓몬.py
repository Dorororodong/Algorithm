def solution(nums):
    n = len(nums)
    set_nums = set(nums)
    set_n = len(set_nums)

    if n / 2 > set_n:
        return set_n

    else:
        return n / 2

print(solution([3,3,3,2,2,4]))