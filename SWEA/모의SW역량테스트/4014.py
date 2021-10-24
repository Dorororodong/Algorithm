'''
각 셀의 숫자는 그 지형의 높이를 의미(지형의 높이는 1 이상 6 이하의 정수)
가로 또는 세로 방향으로 건설할 수 있는 가능성을 확인
활주로는 높이가 동일한 구간에서 건설이 가능
높이가 다른 구간의 경우 활주로가 끊어지기 때문에 경사로를 설치해야만 활주로를 건설 할 수 있음
경사로는 길이가 X( 2 ≤ X ≤ 4 )이고, 높이는 항상 1!!
경사로는 높이 차이가 1 이고 낮은 지형의 높이가 동일하게 경사로의 길이만큼 연속되는 곳에 설치 할 수 있음
'''

# 2시간!

import sys
sys.stdin = open('input.txt')

def DFS_r(r):
    global cnt

    flat_cnt = 1    # 연속 세기 (시작을 위해서 1을 배정)
    flag = 0        # 초기만 0 / 커지면 1 / 작아지면 -1

    if len(set(airstrip[r])) == 1:      # 다같으면 해당! 끝!
        cnt += 1
        return

    else:                               # 아니면
        for i in range(N-1):            # 옆에 놈이랑 비교하면서 진행 / 마지막은 안해줘도 됨
            if abs(airstrip[r][i] - airstrip[r][i+1]) > 1:      # 차이가 2이상이면 의미 없음! 끝!
                return

            else:   # 같으면 연속 +1
                if airstrip[r][i] == airstrip[r][i+1]:
                    flat_cnt += 1

                elif airstrip[r][i] > airstrip[r][i+1]: # 작아지면
                    if flag == 0:                       # 초기면
                        flat_cnt = 1                    # 다시 1로 배정
                        flag = -1                       # 작아짐으로

                    elif flag == -1:                    # 앞에서 작아지고 작아지면
                        if flat_cnt < X:                # 경사로 못 품으면 끝!
                            return

                        else:                           # 경사로 가능하면
                            flat_cnt = 1                # 다시 1로 배정

                    else:                               # 앞에서 커지고 작아지면
                        flat_cnt = 1                    # 다시 1로 배정
                        flag = -1                       # 작아짐으로

                else:                                   # 커지면
                    if flag == 0:                       # 초기면
                        if flat_cnt < X:                # 경사로 못 품으면 끝!
                            return

                        else:                           # 경사로 가능하면
                            flat_cnt = 1                # 다시 1로 배정
                            flag = 1                    # 커짐으로

                    elif flag == -1:                    # 앞에서 작아지고 커지면
                        if flat_cnt < 2 * X:            # 경사로가 2개 필요함 (V자 모형)
                            return                      # 안되면 끝!

                        else:                           # 되면
                            flat_cnt = 1                # 다시 1로 배정
                            flag = 1                    # 커짐으로

                    else:                               # 앞에서 커지고 커지면
                        if flat_cnt < X:                # 경사로 못 품으면 끝!
                            return

                        else:                           # 경사로 가능하면
                            flat_cnt = 1                # 다시 1로 배정

            if i == N - 2:                              # 마지막에서 하나 확인해줘야 됨
                if flag == -1:                          # 바로 감소할때! (그 감소 친구도 확인해줘야함!)
                    if flat_cnt < X:                    # 경사로 못품으면 (사실상 1개니까 flat_cnt = 1)
                        return                          # 끝!

                    else:                               # 되면 pass (안해줘도 되긴함)
                        pass

    cnt += 1        # 모든 경우를 통과했다면 1 증가!


def DFS_c(c):
    global cnt

    flat_cnt = 1
    flag = 0

    for i in range(N-1):
        if abs(airstrip[i][c] - airstrip[i+1][c]) > 1:
            return

        else:
            if airstrip[i][c] == airstrip[i+1][c]:
                flat_cnt += 1

            elif airstrip[i][c] > airstrip[i+1][c]:
                if flag == 0:
                    flat_cnt = 1
                    flag = -1

                elif flag == -1:
                    if flat_cnt < X:
                        return

                    else:
                        flat_cnt = 1

                else:
                    flat_cnt = 1
                    flag = -1

            else:
                if flag == 0:
                    if flat_cnt < X:
                        return

                    else:
                        flat_cnt = 1
                        flag = 1

                elif flag == -1:
                    if flat_cnt < 2 * X:
                        return

                    else:
                        flat_cnt = 1
                        flag = 1

                else:
                    if flat_cnt < X:
                        return

                    else:
                        flat_cnt = 1

        if i == N - 2:
            if flag == -1:
                if flat_cnt < X:
                    return

                else:
                    pass

    cnt += 1


T = int(input())

for tc in range(1, T+1):
    N, X = map(int, input().split())        # N : 한변 길이 / X : 경사로 가로 길이
    airstrip = [list(map(int, input().split())) for _ in range(N)]
    # print(airstrip)

    cnt = 0                 # 해당 갯수 더해줌

    for i in range(N):      # 행방향 조사
        DFS_r(i)

    for j in range(N):      # 열방향 조사
        DFS_c(j)

    print('#{} {}'.format(tc, cnt))

#1 7
#2 4
#3 11
#4 11
#5 15
#6 4
#7 4
#8 1
#9 5
#10 8