'''
우선 순위는 고려하지 않고 왼쪽에서 오른쪽으로 차례대로 계산
게임 판에 적힌 숫자의 개수 N( 3 ≤ N ≤ 12 )
연산자 카드 개수의 총 합은 항상 N - 1
게임 판에 적힌 숫자는 1 이상 9 이하의 정수
수식을 완성할 때 각 연산자 카드를 모두 사용해야
숫자와 숫자 사이에는 연산자가 1 개만 들어가야
나눗셈을 계산 할 때 소수점 이하는 버린다.
입력으로 주어지는 숫자의 순서는 변경할 수 없다.
정답은 만들 수 있는 수식으로 얻은 결과값 중 최댓값과 최솟값의 차이
'''

import sys
sys.stdin = open('input.txt')

def DFS():
    global max_num
    global min_num

    if max_num < :
        max_num =
    if min_num > :
        min_num =

    for i in range(4):
        if operator_num[i] > 0:
            operator_num[i] = operator_num[i] - 1
            if i == 0:
                +
            elif i == 1:
                -
            elif i == 2:
                *
            else:
               int( / )


    return

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    operator_num = list(map(int, input().split()))      # + - * /
    number_list = list(map(int, input().split()))       # 순서보장

    max_num = -987654321
    min_num = 987654321

    DFS()

#1 24
#2 8
#3 144
#4 8
#5 91
#6 150
#7 198
#8 2160
#9 46652
#10 701696


'''
import copy
from collections import deque
from itertools import permutations
import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    operator_num = list(map(int, input().split()))      # + - * /
    number_list = list(map(int, input().split()))       # 순서보장 / popleft, appendleft 이용?
    number_dq = deque(number_list)

    # print(operator_num)
    # print(number_list)

    operator_list = []

    for i in range(4):
        if operator_num[i] == 0:
            continue
        else:
            if i == 0:
                for _ in range(operator_num[i]):
                    operator_list.append('+')
            elif i == 1:
                for _ in range(operator_num[i]):
                    operator_list.append('-')
            elif i == 2:
                for _ in range(operator_num[i]):
                    operator_list.append('*')
            else:
                for _ in range(operator_num[i]):
                    operator_list.append('/')
    # print(operator_list)

    data = permutations(operator_list, N-1)
    data_set = set(data)
    # print(list(data))

    result_list = []

    for i in list(data_set):
        number_dq_c = copy.copy(number_dq)
        for j in i:
            if j == '+':
                number_dq_c.appendleft(number_dq_c.popleft() + number_dq_c.popleft())
            elif j == '-':
                number_dq_c.appendleft(number_dq_c.popleft() - number_dq_c.popleft())
            elif j == '*':
                number_dq_c.appendleft(number_dq_c.popleft() * number_dq_c.popleft())
            else:
                number_dq_c.appendleft(int(number_dq_c.popleft() / number_dq_c.popleft()))

        if len(number_dq_c) == 1:
            if number_dq_c[-1] not in result_list:
                result_list.append(number_dq_c[-1])

    print('#{} {}'.format(tc, max(result_list) - min(result_list)))
'''