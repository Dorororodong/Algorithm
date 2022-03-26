import sys, math

T = int(sys.stdin.readline().rstrip())

for _ in range(1, T+1):
    x1, y1, r1, x2, y2, r2 = map(float, sys.stdin.readline().rstrip().split())

    d = math.dist((x1, y1), (x2, y2))

    if d == 0 and r1 == r2:
        print(-1)

    elif r1 + r2 == d or abs(r1 - r2) == d:
        print(1)

    elif abs(r1 - r2) < d and d < r1 + r2:
        print(2)

    else:
        print(0)