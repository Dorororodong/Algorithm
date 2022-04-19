import sys
N, K = map(int, sys.stdin.readline().rstrip().split())
DP = [[0] * (K+1) for _ in range(N+1)]
stuffs = tuple(map(int, sys.stdin.readline().rstrip().split()) for _ in range(N))   # (무게, 가치)
stuffs = [0] + sorted(stuffs)
# print(stuffs)

for i in range(1, N+1):
    for j in range(1, K+1):
        if j < stuffs[i][0]:
            DP[i][j] = DP[i-1][j]

        else:
            DP[i][j] = max(DP[i - 1][j], DP[i - 1][j - stuffs[i][0]] + stuffs[i][1])

print(DP[N][K])

'''
n, k = map(int, input().split())
products = []
for _ in range(n):
    w, v = map(int, input().split())
    products.append((w,v))

d = [0] * (k+1)
for w, v in products:
    for i in range(k, w-1, -1):
        d[i] = max(d[i], d[i-w] + v)

print(d[-1])
'''