import sys
from math import inf
V, E = map(int, sys.stdin.readline().rstrip().split())
village = [[inf] * V for j in range(V)]
min_dis = inf

for _ in range(E):
    a, b, c = map(int, sys.stdin.readline().rstrip().split())
    village[a-1][b-1] = c

for k in range(V):
    for i in range(V):
        for j in range(V):
            village[i][j] = min(village[i][j], village[i][k] + village[k][j])

for i in range(V):
    if min_dis > village[i][i]:
        min_dis = village[i][i]

if min_dis == inf:
    print(-1)

else:
    print(min_dis)