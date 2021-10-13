N, M = map(int, input().split())

adj = [[0] * (N+1) for _ in range(N+1)]

for i in range(M):
    n1, n2 = map(int, input().split())
    adj[n1][n2] = 1
    adj[n1][n2] = 1
    # print(adj)

