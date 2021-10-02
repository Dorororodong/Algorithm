'''
지도는 N×M크기의 격자로 표현,
위쪽에서 i번째 줄의 왼쪽에서 j번째 칸이 물이면 ‘W’, 땅이면 ‘L’로 표현
어떤 칸에 사람이 있으면, 그 칸의 상하좌우에 있는 칸으로 이동하는 것을 반복하여 다른 칸으로 이동할 수 있다.
단, 격자 밖으로 나가는 이동은 불가능하다.
땅으로 표현된 모든 칸에 대해서,
어떤 물인 칸으로 이동하기 위한 최소 이동 횟수를 구하고 모든 이동 횟수의 합을 출력하는 프로그램을 작성

문자열은 ‘W’또는 ‘L’로만 이루어져 있다.
모든 줄의 문자열을 모두 합쳤을 때, 적어도 하나의 ‘W’는 주어지는 것이 보장
각 테스트 케이스마다 땅으로 표현된 모든 칸에 대해서, 물인 칸으로 이동하기 위한 최소 이동 횟수의 합을 출력
'''

def from_water_to_land(, delta_num)

    return

import sys
sys.stdin = open('input.txt')

T = int(input())

dx = [-1, 1, 0, 0]      # 상 하 좌 우
dy = [0, 0, -1, 1]


for tc in range(1, T+1):
    N, M = map(int, input().split())

    water_park = [list(map(str, ''.join(input()))) for _ in range(N)]
    # print(water_park)

    from_water_to_land(, 1)

    # print('#{} {}'.format(tc, N))

#1 9
#2 4
#3 15