import sys
A, B = map(int, sys.stdin.readline().rstrip().split())
C = int(sys.stdin.readline().rstrip())

A = ((B + C) // 60 + A) % 24
B = (B + C) % 60

print('{} {}'.format(A, B))