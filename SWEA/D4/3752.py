# DP 힌트 얻고, DP 읽음
# 앞에서 했는데 도저히 안되서, 뒤로 하니까... 됨!

import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    score_list = list(map(int, input().split()))

    dp = [0] * (sum(score_list) + 1)        # 0부터 최대까지

    dp[0] = 1                               # 0은 무조건 되니까 체크

    for i in score_list:                    # 0+2 / 2+3, 0+3 / 5+5, 3+5, 2+5, 0+5(중복)
        for j in range(len(dp)-1, -1, -1):
            if dp[j] == 1:
                dp[i+j] = 1

    print('#{} {}'.format(tc, sum(dp)))


'''
from itertools import permutations

import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    score_list = list(map(int, input().split()))
    points_set = set()

    points_set.add(0)

    for i in range(1, len(score_list) + 1):
        data = list(permutations(score_list, i))

        for j in data:
            points_set.add(sum(j))

    print('#{} {}'.format(tc, len(points_set)))
'''


'''
from itertools import permutations

import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    score_list = list(map(int, input().split()))
    score_set = set(score_list)

    perm_list = [i for i in range(0, N+1)]
    # print(perm_list)

    perm = list(permutations(perm_list, len(score_set)))
    # print(perm)

    result = []
    for i in perm:
        for j in range(len(score_set)):
            if i[j] * score_list[j] not in result:
                result.append(i[j] * score_list[j])

    print(len(result))
'''