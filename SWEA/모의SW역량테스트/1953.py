'''
탈주범은 탈출한 지 한 시간 뒤, 맨홀 뚜껑을 통해 지하터널의 어느 한 지점으로 들어갔으며,
탈주범은 시간당 1의 거리를 움직일 수 있다.
터널끼리 연결이 되어 있는 경우 이동이 가능하므로 탈주범이 있을 수 있는 위치의 개수를 계산

0 없을 무
1 상하좌우
2 상하
3 좌우
4 상우
5 하우
6 하좌
7 상좌

탈주범이 있을 수 있는 장소는, 맨홀뚜껑이 위치한 지점을 포함
지하 터널 지도와 맨홀 뚜껑의 위치, 경과된 시간이 주어질 때 탈주범이 위치할 수 있는 장소의 개수를 계산
'''

def check_available(delta):     # 주둥이가 맞는지 확인하는 함수 (그 때 가능한 친구들을 리스트로)
    if delta == (-1, 0):
        return [1, 2, 5, 6]

    elif delta == (1, 0):
        return [1, 2, 4, 7]

    elif delta == (0, -1):
        return [1, 3, 4, 5]

    else:
        return [1, 3, 6, 7]


def check_position(R, C, L):    # L만큼 DFS진행해서 찾을려고

    if L == 0:                  # 0초 되면 정지
        return

    else:
        for i in range(1, 8):   # 1~7까지 종류
            if underground_tunnel[R][C] == i:       # 1~7이면
                for j in delta_dict_xy[i]:          # 그때 가능한 델타를 진행
                    available = check_available(j)  # 가능한 주둥이는 무엇이 있는가
                    NR = R + j[0]                   # 새로운 진행방향
                    NC = C + j[1]
                    if 0 <= NR < N and 0 <= NC < M and underground_tunnel[NR][NC] in available and visited[NR][NC] == 0:    # 범위를 벗어나지 않고, 주둥이 리스트에 있고, 방문을 안했다면
                        visited[NR][NC] = 1     # 방문처리
                        check[NR][NC] = 1       # check처리 (그냥 cnt를 더하면 중복되는 경우{시간이 너무 길어서 다양하게 해당 지점에 위치할 수도 있으니까} 때문에 따로 만듬!)
                        check_position(NR, NC, L-1)     # 시간 1 줄여서 동일하게 재귀
                        visited[NR][NC] = 0     # 나오면 방문처리 복구


import sys
sys.stdin = open('input.txt')

T = int(input())

# 해당 숫자에 대해서 갈 수 있는 delta를 리스트로 받아줌, for문 돌릴려고
delta_dict_xy = {1 : [(-1, 0), (1, 0), (0, -1), (0, 1)], 2 : [(-1, 0), (1, 0)], 3 : [(0, -1), (0, 1)], 4 : [(-1, 0), (0, 1)], 5 : [(1, 0), (0, 1)], 6 : [(1, 0), (0, -1)], 7 : [(-1, 0), (0, -1)]}

for tc in range(1, T+1):
    N, M, R, C, L = map(int, input().split())        # 지하 터널 세로, 가로 / 맨홀 세로, 가로 / 소요시간

    underground_tunnel = [list(map(int, input().split())) for _ in range(N)]
    # print(underground_tunnel)
    cnt = 0                                         # 탈주범이 위치할 수 있는 장소 카운트
    visited = [[0] * M for _ in range(N)]           # 방문 체크
    check = [[0] * M for _ in range(N)]             # 위치하는 장소를 체크


    visited[R][C] = 1                               # 시작 지점 방문
    check[R][C] = 1                                 # 역시 시작지점 체크
    check_position(R, C, L-1)                       # 처음 시작지점에 1시간 씀

    for i in range(N):                              # 체크에 1 되있으면 다 위치할 수 있는 장소임
        for j in range(M):
            if check[i][j] == 1:
                cnt += 1

    print('#{} {}'.format(tc, cnt))

#1 5
#2 15
#3 29
#4 67
#5 71