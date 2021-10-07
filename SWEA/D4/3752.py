import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    score_list = list(map(int, input().split()))



    print('#{} {}'.format(tc, ))


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