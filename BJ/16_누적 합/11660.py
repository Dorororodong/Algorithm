# dp...dp...dp... (수학... 퍼즐... 어디까지 더하고... 어디까지 빼고...)

import sys
N, M = map(int, sys.stdin.readline().rstrip().split())
arr = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(N)]
dp = [[0] * (N+1) for _ in range(N+1)]

for i in range(1, N+1):
    for j in range(1, N+1):
        dp[i][j] = dp[i-1][j] + dp[i][j-1] - dp[i-1][j-1] + arr[i-1][j-1]

for _ in range(M):
    x1, y1, x2, y2 = map(int, sys.stdin.readline().rstrip().split())
    print(dp[x2][y2] - dp[x1-1][y2] - dp[x2][y1-1] + dp[x1-1][y1-1])

'''
import sys
N, M = map(int, sys.stdin.readline().rstrip().split())
arr = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(N)]

for i in arr:
    for j in range(1, N):
        i[j] += i[j-1]

for _ in range(M):
    x1, y1, x2, y2 = map(int, sys.stdin.readline().rstrip().split())
    res = 0

    for i in range(x1 - 1, x2):
        if y1 != 1:
            res += arr[i][y2 - 1] - arr[i][y1 - 2]

        else:
            res += arr[i][y2 - 1]

    print(res)
'''