import sys
N, M = map(int, sys.stdin.readline().split())
maze = list(list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(N))

dp = list([0] * M for _ in range(N))

for i in range(N):
    for j in range(M):
        if i == j == 0:
            dp[i][j] = maze[i][j]

        elif i == 0:
            dp[i][j] = maze[i][j] + dp[i][j-1]

        elif j == 0:
            dp[i][j] = maze[i][j] + dp[i-1][j]

        else:
            dp[i][j] = maze[i][j] + max(dp[i-1][j-1], dp[i][j-1], dp[i-1][j])

print(dp[N-1][M-1])