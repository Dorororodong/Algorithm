import sys

N = int(sys.stdin.readline())
dp = [0] * N
idx = -1
for tc in range(1, N+1):
    color_cost = list(map(int, sys.stdin.readline().split()))
    # print(color_cost)

    if color_cost.index((min(color_cost))) != idx:
        dp[tc] = min(color_cost)
    else:
        color_cost[color_cost.idx(min(color_cost))]
        if color_cost.index((min(color_cost))) != idx:
            dp[tc] = min(color_cost)
        else:
            dp[tc] = max(color_cost)

