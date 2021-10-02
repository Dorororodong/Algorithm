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

'''
from collections import deque

def BFS_land_to_water(idx):
    min_list = []
    Q = deque()
    Q.append(idx)
    visited = [[0] * M for _ in range(N)]
    visited[idx[0]][idx[1]] = 1

    while Q:
        position = Q.pop()

        if water_park[position[0]][position[1]] == 'W':
            min_list.append(position[2])
            continue

        for i in range(4):
            nx = position[0] + dx[i]
            ny = position[1] + dy[i]
            nm = position[2] + 1

            if 0 <= nx < N and 0 <= ny < M and visited[nx][ny] != 1:
                visited[nx][ny] = 1
                Q.append([nx, ny, nm])

    return min(min_list)

import sys
sys.stdin = open('input.txt')

T = int(input())

dx = [-1, 1, 0, 0]      # 상 하 좌 우
dy = [0, 0, -1, 1]

for tc in range(1, T+1):
    N, M = map(int, input().split())
    result = 0
    water_park = [list(map(str, ''.join(input()))) for _ in range(N)]
    # print(water_park)
    land_position = []

    for i in range(N):
        for j in range(M):
            if water_park[i][j] == 'L':
                land_position.append([i, j, 0])

    for i in land_position:
        result += BFS_land_to_water(i)

    print('#{} {}'.format(tc, result))

#1 9
#2 4
#3 15
'''

from collections import deque       # 큐(선입선출) 쓸려고 / 최소 / 가장 근처 / DFS는 깊숙하게, 끝까지

def BFS_water_to_land():            # 물에서 땅으로 / 땅에서 물로하니까 인생망함
    Q = deque()
    result = 0                      # 거리 뽑을 값
    for i in range(N):
        for j in range(M):
            if water_park[i][j] == 'W':     # 물인 곳의 idx 다담고 / visited로 거리계산을 위해 0으로 지정
                Q.append((i, j))            ########## 리스트하면 안되고, 튜플 하면 됨 ##########
                visited[i][j] = 0

    while Q:
        pos = Q.popleft()                   # 왼쪽꺼를 뽑아야 먼저 뽑음

        for i in range(4):                  # 4방향 탐색
            nx = pos[0] + dx[i]
            ny = pos[1] + dy[i]

            if 0 <= nx < N and 0 <= ny < M and visited[nx][ny] == -1:       # 범위 / 방문유무 / 글자유무는 체크안함 (방문유무에서 걸러짐)
                Q.append((nx, ny))      # 해당하는 좌표 넣어줌                 ########## 리스트하면 안되고, 튜플 하면 됨 ##########
                visited[nx][ny] = visited[pos[0]][pos[1]] + 1               # 거리계산을 위해 1씩 증가

    for i in visited:       # 거리 전부다 탐색해서 다 더해버림 : 최소 거리들의 합
        result += sum(i)

    return result

import sys
sys.stdin = open('input.txt')

T = int(input())

dx = [-1, 1, 0, 0]      # 상 하 좌 우
dy = [0, 0, -1, 1]

for tc in range(1, T+1):
    N, M = map(int, input().split())
    water_park = [list(map(str, ''.join(input()))) for _ in range(N)]       # 각각 분해해서 담을려고 (DataFrame처럼)
    # print(water_park)
    visited = [[-1] * M for _ in range(N)]      # visited 이용할려고, 0말고 -1로 함

    print('#{} {}'.format(tc, BFS_water_to_land()))
    # print(visited)

#1 9
#2 4
#3 15