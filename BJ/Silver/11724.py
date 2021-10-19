'''
make_set
'''


'''
DFS
'''
import sys
sys.setrecursionlimit(10e9)

def DFS(x):
    for i in range(1, N+1):
        if visited[i] == 0 and adj[x][i] == 1:
            visited[i] = 1
            DFS(i)

N, M = map(int, input().split())
adj = [[0] * (N+1) for _ in range(N+1)]
visited = [0] * (N+1)

for _ in range(M):
    u, v = map(int, input().split())
    adj[u][v] = 1
    adj[v][u] = 1
    # print(adj)

cnt = 0
for i in range(1, N+1):
    if visited[i] == 0:
        visited[i] = 1
        cnt += 1
        DFS(i)

print(cnt)
