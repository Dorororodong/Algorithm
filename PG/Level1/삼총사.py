from itertools import combinations
def solution(number):
    cnt = 0
    comb = combinations(number, 3)      # O(2^13)

    for i in comb:                      # O(n?!)
        if sum(i) == 0:                 # O(3*n?!)
            cnt += 1
    return cnt

print(solution([-2, 3, 0, 2, -5]))