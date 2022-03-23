import sys
N = int(sys.stdin.readline().rstrip())
G = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(N)]

for k in range(N):

    for i in range(N):
        for j in range(N):
            if G[i][k] and G[k][j]:
                G[i][j] = 1

for i in G:
    print(' '.join(map(str, i)))