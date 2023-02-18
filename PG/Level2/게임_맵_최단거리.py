from collections import deque
dx = [0, 1, -1, 0]
dy = [1, 0, 0, -1]

def solution(maps):
    row = len(maps)
    col = len(maps[0])
    visited = [[False for _ in range(col)] for _ in range(row)]

    def BFS(x, y):
        visited[x][y] = True
        q = deque()
        q.append((x, y))

        while q:
            x, y = q.popleft()

            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]

                if 0 <= nx < row and 0 <= ny < col:
                    if maps[nx][ny] == 1:
                        if visited[nx][ny] == False:
                            visited[nx][ny] = True
                            q.append((nx, ny))
                            maps[nx][ny] = maps[x][y] + 1

    BFS(0, 0)

    ans = maps[row-1][col-1]
    if ans == 1:
        return -1
    else:
        return ans

print(solution([[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]]))
print(solution([[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,0],[0,0,0,0,1]]))


'''
dx = [0, 1, -1, 0]
dy = [1, 0, 0, -1]

def solution(maps):
    min_cnt = 10000
    row = len(maps)
    col = len(maps[0])
    visited = [[False for _ in range(col)] for _ in range(row)]

    def DFS(x, y, cnt):
        nonlocal min_cnt
        visited[x][y] = True

        if x == row - 1 and y == col - 1:
            min_cnt = min(min_cnt, cnt)

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < row and 0 <= ny < col:
                if maps[nx][ny] == 1:
                    if visited[nx][ny] == False:
                        DFS(nx, ny, cnt + 1)
                        visited[nx][ny] = False
    DFS(0, 0, 1)

    if min_cnt == 10000:
        return -1
    else:
        return min_cnt
'''