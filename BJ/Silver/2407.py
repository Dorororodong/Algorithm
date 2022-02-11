import sys, math
n, m = map(int, sys.stdin.readline().rstrip().split())

up, down = 1, 1

up *= math.factorial(n)
down *= math.factorial(n-m)
down *= math.factorial(m)

print(up // down)