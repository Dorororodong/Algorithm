import sys, math
D, H, W = map(int, sys.stdin.readline().rstrip().split())

length = (D ** 2 / (H ** 2 + W ** 2)) ** 0.5

print(math.floor(H * length), math.floor(W * length))