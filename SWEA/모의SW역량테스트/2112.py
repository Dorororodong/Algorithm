'''
보호 필름의 성능을 검사하기 위해 합격기준 K라는 값을 사용한다.
충격은 보호 필름 단면의 세로 방향으로 가해지므로, 세로 방향 셀들의 특성이 중요하다.
단면의 모든 세로방향에 대해서 동일한 특성의 셀들이 K개 이상 연속적으로 있는 경우에만 성능검사를 통과

성능검사에 통과하기 위해서 약품을 사용하여야
약품은 막 별로 투입할 수 있으며 이 경우 투입하는 막의 모든 셀들은 하나의 특성으로 변경된다.
특정 막에 약품 A를 투입하면 막 내의 모든 셀들이 특성 A로 변경되며, 약품 B를 넣게 되면 특성이 모두 특성 B로 변경된다.

두께 D, 가로크기 W인 보호 필름 단면의 정보와 합격기준 K가 주어졌을 때
약품 투입 횟수를 최소로 하여 성능검사를 통과할 수 있는 방법을 찾고, 이때의 약품 투입 횟수를 출력

약품을 투입하지 않고도 성능검사를 통과하는 경우에는 0을 출력

보호 필름의 두께 D는 3이상 13이하의 정수 (3≤D≤13)
보호 필름의 가로크기 W는 1이상 20이하의 정수 (1≤W≤20)
합격기준 K는 1이상 D이하의 정수 (1≤K≤D)
셀이 가질 수 있는 특성은 A, B 두 개만 존재
'''

def check(film, cobination_num):
    global inspect

    for i in combination_num:
        if


def use_drug():
    global inspect

    D_num = [i for i in range(D)]

    for i in range(1, D+1):
        combination_num = combinations(D_num, i)
        check(film, combination_num)


from itertools import combinations
from copy import deepcopy
from pandas import DataFrame
import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    D, W, K = map(int, input().split())     # D : 두께, W : 가로크기, K : 합격기준
    film = [list(map(int, input().split())) for _ in range(D)]  # A : 0, B : 1
    # print(DataFrame(film))
    inspect = 0     # 약품 미사용 : 0 / 약품 사용 : 사용 횟수

    if K == 1:      # K가 1이면 걍 통과 끝
        print('#{} {}'.format(tc, inspect))


    for i in range(W):      # 열
        inspection_list = []
        cnt = 0
        for j in range(D):      # 행 / 위에서 아래로 쭉 검사
            if len(inspection_list) == 0:
                inspection_list.append(film[j][i])      # 시작할땐 0인지 1인지 넣어주고
                cnt += 1        # K와 비교하기 위해 cnt진행
            else:
                if inspection_list[-1] == film[j][i]:   # 같으면
                    cnt += 1        # cnt +1
                    if cnt >= K:    # K이상이면 해당열은 합격
                        break       # 다음 열로 넘어감
                else:                                   # 다르면
                    inspection_list[-1] = film[j][i]    # 해당 숫자 바꿔주고
                    cnt = 1                             # 1로 다시 시작
                    if j > D-K:                         # 남은 것을 봐도 K가 안되는 위치이면
                        use_drug()                      # 약품쓰는 함수로 Go

    print('#{} {}'.format(tc, inspect))

