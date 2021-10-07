'''
N2개의 방이 N×N형태
위에서 i번째 줄의 왼쪽에서 j번째 방에는 1이상 N2 이하의 수 Ai,j가 적혀 있으며
이 숫자는 모든 방에 대해 서로 다르다.
당신이 어떤 방에 있다면, 상하좌우에 있는 다른 방으로 이동할 수 있다.
물론 이동하려는 방이 존재해야 하고
이동하려는 방에 적힌 숫자가 현재 방에 적힌 숫자보다 정확히 1 더 커야 한다.
처음 어떤 수가 적힌 방에서 있어야 가장 많은 개수의 방을 이동할 수 있는지 구하라
'''

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def DFS(x, y, n, c):
    global max_num

    if max_num < c:
        max_num = c

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < N and 0 <= ny < N:
            if room[nx][ny] == n + 1:
                position.append(n)
                DFS(nx, ny, room[nx][ny], c + 1)

import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    room = [list(map(int, input().split())) for _ in range(N)]
    # print(room)

    position = []
    max_num = 0

    for i in range(N):
        for j in range(N):
            DFS(i, j, room[i][j], 1)

    print('#{} {} {}'.format(tc, min(position), max_num))