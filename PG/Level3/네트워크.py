def solution(n, computers):
    cnt = 0
    visited = [False for _ in range(n)]

    def DFS(n, computers, i, visited):
        visited[i] = True

        for connect in range(n):
            if connect != i and computers[i][connect] == 1:
                if visited[connect] == False:
                    DFS(n, computers, connect, visited)

    for i in range(n):
        if visited[i] == False:
            DFS(n, computers, i, visited)
            cnt += 1
    return cnt

print(solution(3, [[1, 1, 0], [1, 1, 1], [0, 1, 1]]))