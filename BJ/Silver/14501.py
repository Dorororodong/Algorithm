import sys
N = int(sys.stdin.readline().rstrip())
timetable = [tuple(map(int, sys.stdin.readline().rstrip().split())) for _ in range(N)]

dp = [0] * (N + 1)

for i in range(N-1, -1, -1):
    if i + timetable[i][0] > N:
        dp[i] = dp[i+1]

    else:
        dp[i] = max(dp[i+1], timetable[i][1] + dp[i + timetable[i][0]])

print(dp[0])