import sys
A, B, C = map(int, sys.stdin.readline().rstrip().split())
D = int(sys.stdin.readline().rstrip())

A = (A + ((D + C) // 60 + B) // 60) % 24
B = (((D + C) // 60 + B) % 60) % 60
C = ((D + C) % 60) % 60

print('{} {} {}'.format(A, B, C))