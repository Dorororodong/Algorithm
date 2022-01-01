import sys
from collections import deque
sys.stdin = open('input.txt')

'''
테스트 케이스에서 1은 벽을 나타내며 0은 길, 2는 출발점, 3은 도착점을 나타낸다.

#부호와 함께 테스트 케이스의 번호를 출력하고, 공백 문자 후 도달 가능 여부를 1 또는 0으로 표시한다 (1 - 가능함, 0 - 가능하지 않음).
'''


dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def BFS(x, y):
    global result

    Q = deque()
    Q.append((x, y))
    visited[x][y] = 1

    while Q:
        x, y = Q.popleft()

        if maze[x][y] == 3:
            result = 1
            return

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < 100 and 0 <= ny < 100 and visited[nx][ny] == 0 and (maze[nx][ny] == 0 or maze[nx][ny] == 3):
                visited[nx][ny] = 1
                Q.append((nx, ny))

for _ in range(10):

    tc = int(input())

    maze = [list(map(int, input())) for _ in range(100)]
    # print(maze)
    visited = [[0] * 100 for _ in range(100)]

    result = 0

    BFS(1, 1)

    print('#{} {}'.format(tc, result))