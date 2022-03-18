def res(x1, y1, r1, x2, y2, r2):
    if math.dist((x1, y1), (x2, y2)) >= r1 + r2:
        return 0

    elif abs(r1 - r2) >= math.dist((x1, y1), (x2, y2)):
        return (min(r1, r2) ** 2) * math.pi

    else:
        phi = (math.acos(
            (r1 ** 2 + (math.dist((x1, y1), (x2, y2)) ** 2) - r2 ** 2) / (2 * r1 * math.dist((x1, y1), (x2, y2))))) * 2
        theta = (math.acos(
            (r2 ** 2 + (math.dist((x1, y1), (x2, y2)) ** 2) - r1 ** 2) / (2 * r2 * math.dist((x1, y1), (x2, y2))))) * 2
        area1 = 0.5 * (r2 ** 2) * (theta - math.sin(theta))
        area2 = 0.5 * (r1 ** 2) * (phi - math.sin(phi))

        return area1 + area2

import sys, math
x1, y1, r1, x2, y2, r2 = map(float, sys.stdin.readline().rstrip().split())

ans = res(x1, y1, r1, x2, y2, r2)

print('{:.3f}'.format(ans))