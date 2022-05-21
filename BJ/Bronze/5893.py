import sys
N = sys.stdin.readline().rstrip()

print(bin(int(N, 2) * 17)[2:])