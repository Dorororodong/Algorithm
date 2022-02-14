import sys
A, I = map(int, sys.stdin.readline().rstrip().split())

print(A * (I-1) + 1)