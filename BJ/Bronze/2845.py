import sys

L, P = map(int, sys.stdin.readline().rstrip().split())
newspaper = list(map(int, sys.stdin.readline().rstrip().split()))
people = L * P

for i in range(5):
    newspaper[i] = newspaper[i] - people

print(*newspaper)