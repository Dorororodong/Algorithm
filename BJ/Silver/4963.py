'''
정사각형으로 이루어져 있는 섬과 바다 지도가 주어진다. 섬의 개수를 세는 프로그램을 작성하시오.
한 정사각형과 가로, 세로 또는 대각선으로 연결되어 있는 사각형은 걸어갈 수 있는 사각형이다.
두 정사각형이 같은 섬에 있으려면, 한 정사각형에서 다른 정사각형으로 걸어서 갈 수 있는 경로가 있어야 한다. 지도는 바다로 둘러싸여 있으며, 지도 밖으로 나갈 수 없다.

입력은 여러 개의 테스트 케이스로 이루어져 있다. 각 테스트 케이스의 첫째 줄에는 지도의 너비 w와 높이 h가 주어진다. w와 h는 50보다 작거나 같은 양의 정수이다.
둘째 줄부터 h개 줄에는 지도가 주어진다. 1은 땅, 0은 바다이다.
입력의 마지막 줄에는 0이 두 개 주어진다.

각 테스트 케이스에 대해서, 섬의 개수를 출력한다.
'''

dx = [1, 0, 1, -1, 1, -1, -1, 0]
dy = [0, 1, 1, 1, -1, -1, 0, -1]

def find_island(x, y):
    visited[x][y] = 1

    for i in range(8):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < h and 0 <= ny < w and jido[nx][ny] == 1 and visited[nx][ny] == 0:
            find_island(nx, ny)

import sys
sys.setrecursionlimit(10**6)    # 쓴 사람도 있고, 안 쓴 사람도 있고... BFS??
                                # [1388은 한방향으로 쭉 가니까 DFS이거, 이건 반경에 섬이 있는지 없는지 체크를 한겹씩 하는 거라서?]

while True:
    w, h = map(int, sys.stdin.readline().rstrip().split())
    if w != 0:
        jido = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(h)]
        # print(jido)

        visited = [[0] * w for _ in range(h)]
        cnt = 0

        for i in range(h):
            for j in range(w):
                if jido[i][j] == 1 and visited[i][j] == 0:
                    cnt += 1
                    find_island(i, j)
        print(cnt)

    else:
        break