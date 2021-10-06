from collections import deque

def BFS(V):
    global cnt

    Q = deque()
    visited[V] = 1
    Q.append(V)

    while Q:
        d = Q.popleft()

        for a in range(1, N+1):
            if visited[a] == 0 and adj[d][a] == 1:
                cnt += 1
                visited[a] = 1
                Q.append(a)


N = int(input())        # 컴퓨터 수
T = int(input())        # 컴퓨터 쌍의 수

adj = [[0] * (N+1) for _ in range(N+1)]
visited = [0] * (N+1)
cnt = 0

for _ in range(T):
    n1, n2 = map(int, input().split())
    adj[n1][n2] = 1
    adj[n2][n1] = 1

BFS(1)
print(cnt)