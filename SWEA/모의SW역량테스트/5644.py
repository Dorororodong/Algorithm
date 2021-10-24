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

def find_value(x1, y1, x2, y2):
    global a_power
    global b_power

    for i in range():



T = int(input())

for tc in range(1, T+1):
    M, A = map(int, input().split())            # M : 이동 시간 / A : 충전소 갯수
    power = [0] * (A + 1)                       # power 목록
    coverage = [0] * (A + 1)                    # 충전 범위 목록
    head = [0] * (A + 1)                        # 본진 좌표
    move_a = list(map(int, input().split()))    # A 이동정보 (M개) / (0, 0) 출발
    move_b = list(map(int, input().split()))    # B 이동정보 (M개) / (9, 9) 출발
    
    for i in range(A):
        X, Y, C, P = map(int, input().split())      # X, Y : 좌표 / C : 충전 범위 / P : 처리량
        power[i+1] = P
        coverage[i+1] = C
        head[i+1] = (X-1, Y-1)

    a_power = 0
    b_power = 0

    find_value(0, 0, 9, 9)

#1 1200
#2 3290
#3 16620
#4 40650
#5 52710