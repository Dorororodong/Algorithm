'''
1번 자석에서 빨간색 화살표 위치에 있는 날의 자성이 N극이면 0점, S극이면 1점을 획득
2번 자석에서 빨간색 화살표 위치에 있는 날의 자성이 N극이면 0점, S극이면 2점을 획득
3번 자석에서 빨간색 화살표 위치에 있는 날의 자성이 N극이면 0점, S극이면 4점을 획득
4번 자석에서 빨간색 화살표 위치에 있는 날의 자성이 N극이면 0점, S극이면 8점을 획득

4개 자석의 자성 정보와 자석을 1칸씩 K번 회전시키려고 할 때,
K번 자석을 회전시킨 후 획득하는 점수의 총 합을 출력

자석의 개수는 4개이며, 각 자석은 8개의 날을 가지고 있다.
자석을 회전시키는 횟수 K( 1 ≤ K ≤ 20 )
하나의 자석이 1칸 회전될 때, 붙어 있는 자석은 서로 붙어 있는 날의 자성이 다를 경우에만 반대방향으로 1칸 회전

자석을 회전시키는 방향은 시계방향이 1, 반시계 방향이 -1

날의 자성은 N극이 0, S극이 1
각 자석의 날 자성정보는 빨간색 화살표 위치의 날부터 시계방향 순서대로
'''

def rotation_play(i):
    if i[0] == 1 and visited[i[0] -1] == 0:         # 첫번째, 방문안했으면
        visited[i[0] - 1] = 1                       # 방문체크
        if i[1] == 1:                               # 시계
            if visited[i[0]] == 1:                  # 2에서 넘어왔다면
                magnet[i[0] - 1] = [magnet[i[0] - 1][-1]] + magnet[i[0] - 1][0:7]   # 회전
            else:                                   # 1이 선택된거면
                if magnet[i[0] - 1][2] == magnet[i[0]][-2]:     # 같으면
                    magnet[i[0] - 1] = [magnet[i[0] - 1][-1]] + magnet[i[0] - 1][0:7]   # 회전
                else:                                           # 다르면
                    magnet[i[0] - 1] = [magnet[i[0] - 1][-1]] + magnet[i[0] - 1][0:7]   # 회전
                    rotation_play((2, -1))          # 2번도 회전(반대반향으로)
        else:                                       # 반시계
            if visited[i[0]] == 1:                  # 2에서 넘어왔다면
                magnet[i[0] - 1] = magnet[i[0] - 1][1:8] + [magnet[i[0] - 1][0]]
            else:                                   # 1이 선택된거면
                if magnet[i[0] - 1][2] == magnet[i[0]][-2]:
                    magnet[i[0] - 1] = magnet[i[0] - 1][1:8] + [magnet[i[0] - 1][0]]
                else:
                    magnet[i[0] - 1] = magnet[i[0] - 1][1:8] + [magnet[i[0] - 1][0]]
                    rotation_play((2, 1))

    elif i[0] == 4 and visited[i[0] -1] == 0:       # 네번째, 방문안했으면
        visited[i[0] - 1] = 1
        if i[1] == 1:
            if visited[i[0]-2] == 1:
                magnet[i[0] - 1] = [magnet[i[0] - 1][-1]] + magnet[i[0] - 1][0:7]
            else:
                if magnet[i[0] - 1][-2] == magnet[i[0] - 2][2]:
                    magnet[i[0] - 1] = [magnet[i[0] - 1][-1]] + magnet[i[0] - 1][0:7]
                else:
                    magnet[i[0] - 1] = [magnet[i[0] - 1][-1]] + magnet[i[0] - 1][0:7]
                    rotation_play((3, -1))
        else:
            if visited[i[0] - 2] == 1:
                magnet[i[0] - 1] = magnet[i[0] - 1][1:8] + [magnet[i[0] - 1][0]]
            else:
                if magnet[i[0] - 1][-2] == magnet[i[0] - 2][2]:
                    magnet[i[0] - 1] = magnet[i[0] - 1][1:8] + [magnet[i[0] - 1][0]]
                else:
                    magnet[i[0] - 1] = magnet[i[0] - 1][1:8] + [magnet[i[0] - 1][0]]
                    rotation_play((3, 1))

    else:                                           # 두/세번째
        if visited[i[0] - 1] == 0:
            visited[i[0] - 1] = 1
            if i[1] == 1:
                if visited[i[0] - 2] == 1:          # 왼쪽에서 넘어왔다면
                    if magnet[i[0] - 1][2] == magnet[i[0]][-2]:
                        magnet[i[0] - 1] = [magnet[i[0] - 1][-1]] + magnet[i[0] - 1][0:7]
                    else:
                        magnet[i[0] - 1] = [magnet[i[0] - 1][-1]] + magnet[i[0] - 1][0:7]
                        rotation_play((i[0]+1, -1))
                elif visited[i[0]] == 1:        # 오른쪽에서 넘어왓따면
                    if magnet[i[0] - 1][-2] == magnet[i[0] -2][2]:
                        magnet[i[0] - 1] = [magnet[i[0] - 1][-1]] + magnet[i[0] - 1][0:7]
                    else:
                        magnet[i[0] - 1] = [magnet[i[0] - 1][-1]] + magnet[i[0] - 1][0:7]
                        rotation_play((i[0]-1, -1))
                else:                           # 내가 시작이라면
                    if magnet[i[0] - 1][2] == magnet[i[0]][-2] and magnet[i[0] - 1][-2] == magnet[i[0] - 2][2]:
                        magnet[i[0] - 1] = [magnet[i[0] - 1][-1]] + magnet[i[0] - 1][0:7]
                    elif magnet[i[0] - 1][2] != magnet[i[0]][-2] and magnet[i[0] - 1][-2] == magnet[i[0] - 2][2]:
                        magnet[i[0] - 1] = [magnet[i[0] - 1][-1]] + magnet[i[0] - 1][0:7]
                        rotation_play((i[0] + 1, -1))
                    elif magnet[i[0] - 1][2] == magnet[i[0]][-2] and magnet[i[0] - 1][-2] != magnet[i[0] - 2][2]:
                        magnet[i[0] - 1] = [magnet[i[0] - 1][-1]] + magnet[i[0] - 1][0:7]
                        rotation_play((i[0] - 1, -1))
                    else:
                        magnet[i[0] - 1] = [magnet[i[0] - 1][-1]] + magnet[i[0] - 1][0:7]
                        rotation_play((i[0] + 1, -1))
                        rotation_play((i[0] - 1, -1))
            else:
                if visited[i[0] - 2] == 1:
                    if magnet[i[0] - 1][2] == magnet[i[0]][-2]:
                        magnet[i[0] - 1] = magnet[i[0] - 1][1:8] + [magnet[i[0] - 1][0]]
                    else:
                        magnet[i[0] - 1] = magnet[i[0] - 1][1:8] + [magnet[i[0] - 1][0]]
                        rotation_play((i[0]+1, 1))
                elif visited[i[0]] == 1:
                    if magnet[i[0] - 1][-2] == magnet[i[0] -2][2]:
                        magnet[i[0] - 1] = magnet[i[0] - 1][1:8] + [magnet[i[0] - 1][0]]
                    else:
                        magnet[i[0] - 1] = magnet[i[0] - 1][1:8] + [magnet[i[0] - 1][0]]
                        rotation_play((i[0]-1, 1))
                else:
                    if magnet[i[0] - 1][2] == magnet[i[0]][-2] and magnet[i[0] - 1][-2] == magnet[i[0] -2][2]:
                        magnet[i[0] - 1] = magnet[i[0] - 1][1:8] + [magnet[i[0] - 1][0]]
                    elif magnet[i[0] - 1][2] != magnet[i[0]][-2] and magnet[i[0] - 1][-2] == magnet[i[0] -2][2]:
                        magnet[i[0] - 1] = magnet[i[0] - 1][1:8] + [magnet[i[0] - 1][0]]
                        rotation_play((i[0]+1, 1))
                    elif magnet[i[0] - 1][2] == magnet[i[0]][-2] and magnet[i[0] - 1][-2] != magnet[i[0] -2][2]:
                        magnet[i[0] - 1] = magnet[i[0] - 1][1:8] + [magnet[i[0] - 1][0]]
                        rotation_play((i[0]-1, 1))
                    else:
                        magnet[i[0] - 1] = magnet[i[0] - 1][1:8] + [magnet[i[0] - 1][0]]
                        rotation_play((i[0]+1, 1))
                        rotation_play((i[0]-1, 1))

import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    K = int(input())                                                    # 회전 횟수
    magnet = [list(map(int, input().split())) for _ in range(4)]        # 자석 정보
    rotate = [tuple(map(int, input().split())) for _ in range(K)]       # [몇번 자석, 어느 방향] K(횟수)만큼 있음
    # print(magnet)
    # print(rotate)
    total_score = 0

    for r in rotate:
        visited = [0] * 4       # 방문 체크, 역으로 다시 안가게
        rotation_play(r)        # 자석번호(idx+1), 회전방향

    if magnet[0][0] == 1:       # 최종 계산
        total_score += 1
    if magnet[1][0] == 1:
        total_score += 2
    if magnet[2][0] == 1:
        total_score += 4
    if magnet[3][0] == 1:
        total_score += 8

    print('#{} {}'.format(tc, total_score))

'''
#1 2
#2 6
#3 2
#4 7
#5 5
#6 15
#7 6
#8 10
#9 13
#10 0
'''