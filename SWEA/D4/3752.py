# import sys
# sys.stdin = open('input.txt')
#
# def perm(n, m, k):
#
#     if n == k:                              # 모든 자리가 결정이 됐다면
#         if sum(p) in result_list:
#             return
#         else:
#             result_list.append(sum(p))
#             return
#     else:
#         for i in range(m):                  # 주어진 숫자의 개수만큼 반복을 돌며
#             if not u[i]:                    # 아직 사용하지 않은 자리라면
#                 u[i] = 1                    # 사용했다고 표시하고
#                 p[k] = score_list[i]        # 그 숫자를 넣고
#                 perm(n, m, k+1)             # 다음 자리를 결정하러 가자
#                 u[i] = 0                    # 돌아와서 원상복구
#
# T = int(input())
#
# for tc in range(1, T+1):
#     N = int(input())
#     score_list = list(map(int, input().split()))
#     result_list = []
#
#     p = [0] * N
#     u = [0] * N
#     for i in range(1, N+1):
#         perm(i, N, 0)
#
#     print('#{} {}'.format(tc, len(result_list) + 1))
#
#
#     """
#     :param n: 순열의 길이
#     :param m:
#     :param k: 결정 할 위치
#     :return:
#     """

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