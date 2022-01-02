import sys

N, M = map(int, sys.stdin.readline().rstrip().split())

arr1 = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(N)]
arr2 = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(N)]

for i in range(N):
    for j in range(M):
        arr1[i][j] += arr2[i][j]

for k in arr1:
    print(*k)