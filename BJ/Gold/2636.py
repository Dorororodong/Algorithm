dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def bfs():
    visited = [[0] * M for _ in range(N)]

    q = deque()
    q.append([0, 0])
    visited[0][0] = 1
    del_cnt = 0

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < N and 0 <= ny < M:
                if visited[nx][ny] == 0:

                    if cheese[nx][ny] == 0:         # 노치즈 (이동해서 계속 살펴볼 경우) [가장자리, 바깥부분]
                        visited[nx][ny] = 1
                        q.append([nx, ny])          # 노치즈인 곳은 다 봐야하니까 (돌면서)

                    elif cheese[nx][ny] == 1:       # 예스치즈 (q에 안넣음, 넣으면 안쪽 치즈도 파괴됨)
                        visited[nx][ny] = 1
                        cheese[nx][ny] = 0          # 치즈 파괴
                        del_cnt += 1

    del_cheese.append(del_cnt)  # 초당 없앤 치즈갯수 넣어주기
    return del_cnt

import sys
from collections import deque
N, M = map(int, sys.stdin.readline().rstrip().split())
cheese = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(N)]

del_cheese = []
time = 0

while True:
    time += 1
    cnt = bfs()

    if cnt == 0:
        break

print(time-1)               # 마지막은 다 없어졌는지 확인하는 과정이니까 -1
print(del_cheese[-2])       # 역시 마지막은 루프를 나올 0이니까 그 앞에꺼!