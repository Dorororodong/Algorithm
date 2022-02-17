import sys
T = int(sys.stdin.readline().rstrip())

for _ in range(T):
    N = int(sys.stdin.readline().rstrip())

    MT = [list(sys.stdin.readline().rstrip().split()) for _ in range(N)]

    MT.sort(key= lambda x : int(x[1]))

    print(MT[-1][0])