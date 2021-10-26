from collections import deque

import sys
sys.stdin = open('input.txt')
# input = sys.stdin.readline

def minus_one(m, c):
    if 0 <= m-1 <= 100000:
        if visited[m-1] == -1:
            visited[m-1] = 0
            Q.append((m-1, c+1))

def plus_one(m, c):
    if 0 <= m+1 <= 100000:
        if visited[m+1] == -1:
            visited[m+1] = 0
            Q.append((m+1, c+1))

def teleportation(m, c):
    if 0 <= 2 * m <= 100000:
        if visited[2 * m] == -1:
            visited[2 * m] = 0
            Q.append((2 * m, c+1))

def BFS(n, k, c):
    Q.append((n, c))
    visited[n] = 0

    while Q:

        n, c = Q.popleft()

        if n == k:
            return c

        minus_one(n, c)
        plus_one(n, c)
        teleportation(n, c)



def BFS_route(n, k, c, f):
    global cnt_result

    Q.append((n, c))

    while Q:
        n, c = Q.popleft()

        num_set.add(n)

        if n < 0 or n > 100000 or k < 0 or k > 100000:
            return

        if c > f:
            return

        if n == k and c == f:
            cnt_result += 1

        if n-1 not in num_set:
            Q.append((n - 1, c + 1))

        if n+1 not in num_set:
            Q.append((n + 1, c + 1))

        if 2 * n not in num_set:
            Q.append((2 * n, c + 1))


N, K = map(int, input().split())

visited = [-1] * 100001
Q = deque()
min_result = BFS(N, K, 0)
print(min_result)

Q = deque()
num_set = set()
cnt_result = 0
BFS_route(N, K, 0, min_result)
print(cnt_result)