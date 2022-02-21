# recursionlimit은 안쓰는게 맞다고 생각한다... 할 수 있는 문제를 내지 않을까? 아니면 다른 풀이로라도 가능한 문제를!
def DFS(n):
    for j in range(1, N+1):
        if node[n][j] == 1 and visited[j] == 0:
            visited[j] = 1
            DFS(j)

import sys
N, M = map(int, sys.stdin.readline().rstrip().split())  # 정점 갯수 / 간선 갯수
node = [[0] * (N + 1) for _ in range(N + 1)]
visited = [0] * (N + 1)

for _ in range(M):
    u, v = map(int, sys.stdin.readline().rstrip().split())
    node[u][v] = 1
    node[v][u] = 1

cnt = 0
for i in range(1, N+1):
    if visited[i] == 0:
        visited[i] = 1
        DFS(i)
        cnt += 1

print(cnt)

'''
# BFS / 인접 리스트 (인접 행렬만 고집 하지말고...)
import sys
N,M=map(int,sys.stdin.readline().split())
graph=[[]for i in range(N+1)]

for i in range(M):
    a,b=map(int,sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)
    
visit_list=[0]*(N+1)

def bfs(v):
    q=[v]
    
    while q:
        v=q.pop(0)
        
        for i in graph[v]:
            if visit_list[i]==0:
                q.append(i)
                visit_list[i]=1

answer=0
for i in range(1,N+1):
    if visit_list[i]==0:
        bfs(i)
        answer+=1

sys.stdout.write(str(answer))
'''