# 플로이드-와샬 : 최단거리 알고리즘, BFS는 한 정점에서터 모든 정점으로의 최단거리 / 플로이드와샬은 그래프에서 모든 정점 사이의 최단거리
import sys
from math import inf        # 무한으로~
n = int(sys.stdin.readline().rstrip())
m = int(sys.stdin.readline().rstrip())

cost = [[inf if i != j else 0 for i in range(n)] for j in range(n)]

for _ in range(m):
    a, b, c = map(int, sys.stdin.readline().rstrip().split())
    cost[a-1][b-1] = min(cost[a-1][b-1], c)

for k in range(n):          # 경유지!
    cost[k][k] = 0

    for i in range(n):      # 출발지!
        for j in range(n):  # 목적지!
            cost[i][j] = min(cost[i][j], cost[i][k] + cost[k][j])

for i in cost:
    for j in i:
        if j == inf:        # 여전히 안바뀐건 경로가 없다는 것!
            print(0, end=' ')

        else:
            print(j, end=' ')

    print()