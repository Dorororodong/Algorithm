import sys
N, M, K = map(int, sys.stdin.readline().rstrip().split())

print(K // M, K % M)