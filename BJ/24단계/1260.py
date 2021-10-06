'''
그래프를 DFS로 탐색한 결과와 BFS로 탐색한 결과를 출력하는 프로그램을 작성하시오.
단, 방문할 수 있는 정점이 여러 개인 경우에는 정점 번호가 작은 것을 먼저 방문,
더 이상 방문할 수 있는 점이 없는 경우 종료. 정점 번호는 1번부터 N번 까지

간선은 양방향!!
'''


from collections import deque


def DFS(V):
    visited_d[V] = 1
    DFS_list.append(V)

    for a in range(1, N+1):
        # if len(DFS_list) == N:
        #     break
        if visited_d[a] == 0 and adj[V][a] == 1:
            DFS(a)

    return DFS_list


def BFS(V):
    Q = deque()
    Q.append(V)
    visited_b[V] = 1

    while Q:
        d = Q.popleft()
        BFS_list.append(d)

        for a in range(1, N+1):
            if visited_b[a] == 0 and adj[d][a] == 1:
                visited_b[a] = 1
                Q.append(a)

    return BFS_list


N, M, V = map(int, input().split())         # N : 정점 갯수 / M : 간선 갯수 / V : 탐색을 시작할 정점 번호

adj = [[0] * (N + 1) for _ in range(N + 1)]
visited_d = [0] * (N + 1)                     # 방문여부 리스트 생성 (리스트 같이 쓰면 안됨, 따로)
visited_b = [0] * (N + 1)                     # 방문여부 리스트 생성
DFS_list = []                               # 탐색 담아서 출력할려고
BFS_list = []                               # 탐색 담아서 출력할려고

for _ in range(M):
    n1, n2 = map(int, input().split())      # 정보 받아서 인접행렬에 반영
    adj[n1][n2] = 1
    adj[n2][n1] = 1

# print(adj)
print(*DFS(V))
print(*BFS(V))