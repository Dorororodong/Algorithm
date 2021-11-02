import sys
sys.stdin = open('input.txt')

N = int(input())
result = 0
idx = -1
for tc in range(N):
    color_cost = list(map(int, input().split()))
    # print(color_cost)

    if color_cost.index(min(color_cost)) != idx:
        result += min(color_cost)
        idx = color_cost.index(min(color_cost))
    else:
        color_cost[idx] = 1001
        result += min(color_cost)
        idx = color_cost.index(min(color_cost))

print(result)