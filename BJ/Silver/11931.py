import sys
N = int(sys.stdin.readline().rstrip())
res = [int(sys.stdin.readline().rstrip()) for _ in range(N)]
res.sort(reverse=True)

for i in res:
    print(i)