'''
지도의 가로, 세로 크기는 10
사용자는 총 2명
사용자A는 지도의 (1, 1) 지점에서, 사용자B는 지도의 (10, 10) 지점에서 출발
(20 ≤ M ≤ 100)
(1 ≤ A ≤ 8)
(1 ≤ C ≤ 4)
짝수이다. (10 ≤ P ≤ 500)
사용자의 초기 위치(0초)부터 충전을 할 수 있다.
같은 위치에 2개 이상의 BC가 설치된 경우는 없다.
사용자 A, B가 동시에 같은 위치로 이동할 수는 있다.
사용자가 지도 밖으로 이동하는 경우는 없다.
'''

import sys
sys.stdin = open('input.txt')

# 0 : 이동 X / 1 : 상 / 2 : 우 / 3 : 하 / 4 : 좌
delta = [(0, 0), (-1, 0), (0, 1), (1, 0), (0, -1)]

def find_max_power(x1, y1, x2, y2):
    global all_power

    for i in range(len(move_a)):
        P_list_1 = [0] * A
        P_list_2 = [0] * A

        x1 += delta[move_a[i]][0]
        y1 += delta[move_a[i]][1]

        x2 += delta[move_b[i]][0]
        y2 += delta[move_b[i]][1]

        for j in range(A):
            if abs(x1-head[j][0]) + abs(y1-head[j][1]) <= coverage[j]:
                P_list_1[j] = power[j]

            if abs(x2 - head[j][0]) + abs(y2 - head[j][1]) <= coverage[j]:
                P_list_2[j] = power[j]

        if max(P_list_1) != max(P_list_2):
            all_power += max(P_list_1)
            all_power += max(P_list_2)

        else:
            pass
        # 여기 모르겠음



T = int(input())

for tc in range(1, T+1):
    M, A = map(int, input().split())            # M : 이동 시간 / A : 충전소 갯수
    power = [0] * A                             # power 목록
    coverage = [0] * A                          # 충전 범위 목록
    head = [0] * A                              # 본진 좌표

    move_a = [0] + list(map(int, input().split()))    # A 이동정보 (M개) / (1, 1) 출발
    move_b = [0] + list(map(int, input().split()))    # B 이동정보 (M개) / (10, 10) 출발
    
    for i in range(A):
        X, Y, C, P = map(int, input().split())      # X, Y : 좌표 / C : 충전 범위 / P : 처리량
        power[i] = P
        coverage[i] = C
        head[i] = (X, Y)

    # print(power)
    # print(coverage)
    # print(head)
    # print(move_a)
    # print(move_b)
    all_power = 0
    find_max_power(1, 1, 10, 10)

    print('#{} {}'.format(tc, all_power))

#1 1200
#2 3290
#3 16620
#4 40650
#5 52710