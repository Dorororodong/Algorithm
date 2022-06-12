import sys
T = int(sys.stdin.readline().rstrip())

for _ in range(T):
    a, b, c, d, e = map(float, sys.stdin.readline().rstrip().split())

    print('{}{:.2f}'.format('$', a * 350.34 + b * 230.90 + c * 190.55 + d * 125.30 + e * 180.90))