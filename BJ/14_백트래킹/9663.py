# 참고 : https://velog.io/@uoayop/BOJ-9663-N-Queen-Python

import sys
N = int(sys.stdin.readline().rstrip())

cnt = 0
chess = [0] * N
visited = [False] * N

# 같은 열 / 대각 부분 조사!
def promising(n):
    for i in range(n):
        if chess[n] == chess[i] or abs(chess[n] - chess[i]) == n - i:
            return False

    return True

def n_queen(n):
    global cnt

    if n == N:
        cnt += 1
        return

    for i in range(N):
        if visited[i]:
            continue

        chess[n] = i

        if promising(n):
            visited[i] = True
            n_queen(n+1)
            visited[i] = False

n_queen(0)

print(cnt)