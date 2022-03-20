w_start = ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B']
b_start = ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W']

def start_w(x, y):
    global min_cnt
    cnt = 0
    seq = 0

    for i in range(x, x + 8):
        seq += 1
        idx = 0
        for j in range(y, y + 8):
            if seq % 2:
                if chess[i][j] != w_start[idx]:
                    cnt += 1
                idx += 1

            else:
                if chess[i][j] != b_start[idx]:
                    cnt += 1
                idx += 1

    if min_cnt > cnt:
        min_cnt = cnt

def start_b(x, y):
    global min_cnt
    cnt = 0
    seq = 0

    for i in range(x, x + 8):
        seq += 1
        idx = 0
        for j in range(y, y + 8):
            if seq % 2:
                if chess[i][j] != b_start[idx]:
                    cnt += 1
                idx += 1

            else:
                if chess[i][j] != w_start[idx]:
                    cnt += 1
                idx += 1

    if min_cnt > cnt:
        min_cnt = cnt

import sys
M, N = map(int, sys.stdin.readline().rstrip().split())
chess = [list(sys.stdin.readline().rstrip()) for _ in range(M)]

min_cnt = 65

for i in range(M - 7):
    for j in range(N - 7):
        start_w(i, j)
        start_b(i, j)

print(min_cnt)