'''
4×4 크기의 격자판
격자판의 각 격자칸에는 0부터 9 사이의 숫자가 적혀 있다.
격자판의 임의의 위치에서 시작해서
동서남북 네 방향으로 인접한 격자로 총 여섯 번 이동하면서
각 칸에 적혀있는 숫자를 차례대로 이어 붙이면 7자리의 수가 된다.
이동을 할 때에는 한 번 거쳤던 격자칸을 다시 거쳐도 되며
0으로 시작하는 0102001과 같은 수를 만들 수도 있다.
단, 격자판을 벗어나는 이동은 가능하지 않다고 가정한다.
격자판이 주어졌을 때
만들 수 있는 서로 다른 일곱 자리 수들의 개수를 구하는 프로그램을 작성하시오.
'''

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def DFS(x, y, w):

    if len(w) == 7:
        word.add(w)     # set()은 add로 추가
        return

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < 4 and 0 <= ny < 4:
            DFS(nx, ny, w + grating[nx][ny])

import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    grating = [list(input().split()) for _ in range(4)]
    # print(grating)

    word = set()        # 중복 제거

    for i in range(4):
        for j in range(4):
            DFS(i, j, grating[i][j])        # 가급적이면 매개변수로 다 넣어보자

    print('#{} {}'.format(tc, len(word)))