'''
임의의 자석을 1 칸씩 K 번 회전시키려고 해보니,
하나의 자석이 1 칸 회전될 때,
붙어 있는 자석은 서로 붙어 있는 날의 자성과 다를 경우에만
인력에 의해 반대 방향으로 1칸 회전

1번 자석에서 빨간색 화살표 위치에 있는 날의 자성이 N극이면 0점,
S극이면 1점을 획득한다.
2번 자석에서 빨간색 화살표 위치에 있는 날의 자성이 N극이면 0점,
S극이면 2점을 획득한다.
3번 자석에서 빨간색 화살표 위치에 있는 날의 자성이 N극이면 0점,
S극이면 4점을 획득한다.
4번 자석에서 빨간색 화살표 위치에 있는 날의 자성이 N극이면 0점,
S극이면 8점을 획득한다.

4개 자석의 자성 정보와 자석을 1칸씩 K번 회전시키려고 할 때,
K번 자석을 회전시킨 후 획득하는 점수의 총 합을 출력

자석의 개수는 4개이며, 각 자석은 8개의 날을 가지고 있다.
자석을 회전시키는 횟수 K( 1 ≤ K ≤ 20 )
하나의 자석이 1칸 회전될 때,
붙어 있는 자석은 서로 붙어 있는 날의 자성이 다를 경우에만 반대방향으로 1칸 회전
자석을 회전시키는 방향은 시계방향이 1, 반시계 방향이 -1
날의 자성은 N극이 0, S극이 1
각 자석의 날 자성정보는 빨간색 화살표 위치의 날부터 시계방향 순서대로
'''

def rotation_play(rotate):
    return

import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    K = int(input())                                                    # 회전 횟수
    magnet = [list(map(int, input().split())) for _ in range(4)]        # 자석 정보
    rotate = [list(map(int, input().split())) for _ in range(K)]        # [몇번 자석, 어느 방향] K(횟수)만큼 있음
    # print(magnet)
    # print(rotate)

    total_score = 0

    for i in rotate:
        rotation_play(i)

    #
    #     if i[0] == 1:       # 1번 자석을 회전한다면
    #         if i[1] == 1:       # 시계 방향
    #             if magnet[i[0]-1][2] == magnet[i[0]][-2]:       # 마주 닿는 부분이 같다면, 회전 안함
    #                 magnet[i[0]-1] = [magnet[i[0]-1][-1]] + magnet[i[0]-1][0:7]
    #
    #             else:       # 마주 닿는 부분이 다르면, 회전 함
    #                 magnet[i[0] - 1] = [magnet[i[0] - 1][-1]] + magnet[i[0] - 1][0:7]       # 나는 시계
    #                 magnet[i[0]] = magnet[i[0]][1:8] + [magnet[i[0]][0]]                    # 너는 반시계
    #
    #         else:       # 반시계 방향
    #             if magnet[i[0] - 1][2] == magnet[i[0]][-2]:     # 마주 닿는 부분이 같다면, 회전 안함
    #                 magnet[i[0] - 1] = magnet[i[0]-1][1:8] + [magnet[i[0]-1][0]]
    #
    #             else:       # 마주 닿는 부분이 다르면, 회전 함
    #                 magnet[i[0] - 1] = magnet[i[0] - 1][1:8] + [magnet[i[0] - 1][0]]        # 나는 반시계
    #                 magnet[i[0]] = [magnet[i[0]][-1]] + magnet[i[0]][0:7]                   # 너는 시계
    #
    #
    #     elif i[0] == 4:     # 4번 자석을 회전한다면
    #         if i[1] == 1:       # 시계 방향
    #             if magnet[i[0]-1][2] == magnet[i[0]-2][-2]:       # 마주 닿는 부분이 같다면, 회전 안함
    #                 magnet[i[0]-1] = [magnet[i[0]-1][-1]] + magnet[i[0]-1][0:7]
    #
    #             else:       # 마주 닿는 부분이 다르면, 회전 함
    #                 magnet[i[0] - 1] = [magnet[i[0] - 1][-1]] + magnet[i[0] - 1][0:7]       # 나는 시계
    #                 magnet[i[0]-2] = magnet[i[0]-2][1:8] + [magnet[i[0]-2][0]]              # 너는 반시계
    #
    #         else:       # 반시계 방향
    #             if magnet[i[0] - 1][2] == magnet[i[0]-2][-2]:     # 마주 닿는 부분이 같다면, 회전 안함
    #                 magnet[i[0] - 1] = magnet[i[0]-1][1:8] + [magnet[i[0]-1][0]]
    #
    #             else:       # 마주 닿는 부분이 다르면, 회전 함
    #                 magnet[i[0] - 1] = magnet[i[0] - 1][1:8] + [magnet[i[0] - 1][0]]        # 나는 반시계
    #                 magnet[i[0]-2] = [magnet[i[0]-2][-1]] + magnet[i[0]-2][0:7]             # 너는 시계
    #
    #
    #     else:       # 2, 3번 자석을 회전한다면
    #         if i[1] == 1:       # 시계 방향
    #             if magnet[i[0]-1][2] == magnet[i[0]-2][-2] and magnet[i[0]-1][2] == magnet[i[0]][-2]:       # 마주 닿는 부분이 같같
    #                 magnet[i[0]-1] = [magnet[i[0]-1][-1]] + magnet[i[0]-1][0:7]
    #
    #             elif magnet[i[0]-1][2] == magnet[i[0]-2][-2] and magnet[i[0]-1][2] != magnet[i[0]][-2]:     # 마주 닿는 부분이 같다
    #                 magnet[i[0]-1] = [magnet[i[0]-1][-1]] + magnet[i[0]-1][0:7]
    #                 magnet[i[0]] = magnet[i[0]][1:8] + [magnet[i[0]][0]]
    #
    #
    #             elif magnet[i[0] - 1][2] != magnet[i[0] - 2][-2] and magnet[i[0] - 1][2] == magnet[i[0]][-2]:       # 마주 닿는 부분이 다같
    #                 magnet[i[0]-1] = [magnet[i[0]-1][-1]] + magnet[i[0]-1][0:7]
    #                 magnet[i[0] - 2] = magnet[i[0]-2][1:8] + [magnet[i[0]-2][0]]
    #
    #
    #             else:       # 마주 닿는 부분이 다다
    #                 magnet[i[0]-1] = [magnet[i[0]-1][-1]] + magnet[i[0]-1][0:7]
    #                 magnet[i[0]] = magnet[i[0]][1:8] + [magnet[i[0]][0]]
    #                 magnet[i[0] - 2] = magnet[i[0]-2][1:8] + [magnet[i[0]-2][0]]
    #
    #
    #
    #         else:       # 반시계 방향
    #             if magnet[i[0] - 1][2] == magnet[i[0] - 2][-2] and magnet[i[0] - 1][2] == magnet[i[0]][-2]:  # 마주 닿는 부분이 같같
    #                 magnet[i[0] - 1] = magnet[i[0]-1][1:8] + [magnet[i[0]-1][0]]
    #
    #             elif magnet[i[0] - 1][2] == magnet[i[0] - 2][-2] and magnet[i[0] - 1][2] != magnet[i[0]][-2]:  # 마주 닿는 부분이 같다
    #                 magnet[i[0] - 1] = magnet[i[0]-1][1:8] + [magnet[i[0]-1][0]]
    #                 magnet[i[0]] = [magnet[i[0]][-1]] + magnet[i[0]][0:7]
    #
    #
    #             elif magnet[i[0] - 1][2] != magnet[i[0] - 2][-2] and magnet[i[0] - 1][2] == magnet[i[0]][-2]:  # 마주 닿는 부분이 다같
    #                 magnet[i[0] - 1] = magnet[i[0]-1][1:8] + [magnet[i[0]-1][0]]
    #                 magnet[i[0]-2] = [magnet[i[0]-2][-1]] + magnet[i[0]-2][0:7]
    #
    #
    #             else:  # 마주 닿는 부분이 다다
    #                 magnet[i[0] - 1] = magnet[i[0]-1][1:8] + [magnet[i[0]-1][0]]
    #                 magnet[i[0]-2] = [magnet[i[0]-2][-1]] + magnet[i[0]-2][0:7]
    #                 magnet[i[0]] = [magnet[i[0]][-1]] + magnet[i[0]][0:7]
    #
    #
    # for i in range(4):
    #     if magnet[i][0] == 1 and i == 0:
    #         total_score += 1
    #     if magnet[i][0] == 1 and i == 1:
    #         total_score += 2
    #     if magnet[i][0] == 1 and i == 2:
    #         total_score += 4
    #     if magnet[i][0] == 1 and i == 3:
    #         total_score += 8

    print('#{} {}'.format(tc, total_score))