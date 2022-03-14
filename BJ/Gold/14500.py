# 때로는 단순한게 최고인 법...
def one_to_four(x, y):
    global max_result
    for i in range(x):
        for j in range(y):
            if sum(tetromino[i][j:j+4]) > max_result:
                max_result = sum(tetromino[i][j:j+4])

def four_to_one(x, y):
    global max_result
    for i in range(x):
        for j in range(y):
            result = 0
            for k in range(4):
                result += tetromino[i+k][j]

            if result > max_result:
                max_result = result

def two_to_two(x, y):
    global max_result
    for i in range(x):
        for j in range(y):
            result = 0
            for k in range(2):
                for m in range(2):
                    result += tetromino[i+k][j+m]

            if result > max_result:
                max_result = result

def three_to_two(x, y):
    global max_result
    for i in range(x):
        for j in range(y):
            result = []
            for k in range(3):
                for m in range(2):
                    result.append(tetromino[i+k][j+m])

            if sum(result) - result[1] - result[3] > max_result:
                max_result = sum(result) - result[1] - result[3]

            if sum(result) - result[2] - result[4] > max_result:
                max_result = sum(result) - result[2] - result[4]

            if sum(result) - result[3] - result[5] > max_result:
                max_result = sum(result) - result[3] - result[5]

            if sum(result) - result[0] - result[2] > max_result:
                max_result = sum(result) - result[0] - result[2]

            if sum(result) - result[1] - result[4] > max_result:
                max_result = sum(result) - result[1] - result[4]

            if sum(result) - result[0] - result[5] > max_result:
                max_result = sum(result) - result[0] - result[5]

            if sum(result) - result[0] - result[4] > max_result:
                max_result = sum(result) - result[0] - result[4]

            if sum(result) - result[1] - result[5] > max_result:
                max_result = sum(result) - result[1] - result[5]

def two_to_three(x, y):
    global max_result
    for i in range(x):
        for j in range(y):
            result = []
            for k in range(2):
                for m in range(3):
                    result.append(tetromino[i + k][j + m])

            if sum(result) - result[0] - result[5] > max_result:
                max_result = sum(result) - result[0] - result[5]

            if sum(result) - result[2] - result[3] > max_result:
                max_result = sum(result) - result[2] - result[3]

            if sum(result) - result[0] - result[1] > max_result:
                max_result = sum(result) - result[0] - result[1]

            if sum(result) - result[4] - result[5] > max_result:
                max_result = sum(result) - result[4] - result[5]

            if sum(result) - result[1] - result[2] > max_result:
                max_result = sum(result) - result[1] - result[2]

            if sum(result) - result[3] - result[4] > max_result:
                max_result = sum(result) - result[3] - result[4]

            if sum(result) - result[3] - result[5] > max_result:
                max_result = sum(result) - result[3] - result[5]

            if sum(result) - result[0] - result[2] > max_result:
                max_result = sum(result) - result[0] - result[2]

import sys
N, M = map(int, sys.stdin.readline().rstrip().split())
tetromino = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(N)]

max_result = -1

one_to_four(N, M-3)
four_to_one(N-3, M)
two_to_two(N-1, M-1)
three_to_two(N-2, M-1)
two_to_three(N-1, M-2)

print(max_result)

'''
# 깔끔한 dfs and ㅗ모양 풀이
import sys
input = sys.stdin.readline

# 상, 하, 좌, 우
move = [(0, 1), (0, -1), (1, 0), (-1, 0)]

# INPUT
N, M = map(int, input().split())
board = [list(map(int,input().split())) for _ in range(N)]
visited = [[False] * M for _ in range(N)]

# 최대값 변수
maxValue = 0

# ㅗ, ㅜ, ㅓ, ㅏ 제외한 모양들 최대값 계산
def dfs(i, j, dsum, cnt):
    global maxValue
    # 모양 완성되었을 때 최대값 계산
    if cnt == 4:
        maxValue = max(maxValue, dsum)
        return

    # 상, 하, 좌, 우로 이동
    for n in range(4):
        ni = i+move[n][0]
        nj = j+move[n][1]
        if 0 <= ni < N and 0 <= nj < M and not visited[ni][nj]:
            # 방문 표시 및 제거
            visited[ni][nj] = True
            dfs(ni, nj, dsum + board[ni][nj], cnt+1)
            visited[ni][nj] = False


# ㅗ, ㅜ, ㅓ, ㅏ 모양의 최대값 계산
def exce(i, j):
    global maxValue
    for n in range(4):
        # 초기값은 시작지점의 값으로 지정
        tmp = board[i][j]
        for k in range(3):
            # move 배열의 요소를 3개씩 사용할 수 있도록 인덱스 계산
            # 012, 123, 230, 301
            t = (n+k)%4
            ni = i+move[t][0]
            nj = j+move[t][1]

            if not (0 <= ni < N and 0 <= nj < M):
                tmp = 0
                break
            tmp += board[ni][nj]
        # 최대값 계산
        maxValue = max(maxValue, tmp)


for i in range(N):
    for j in range(M):
        # 시작점 visited 표시
        visited[i][j] = True
        dfs(i, j, board[i][j], 1)
        visited[i][j] = False

        exce(i, j)

print(maxValue)
'''