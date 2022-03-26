import sys
import math

N = int(sys.stdin.readline().rstrip())

rings = list(map(int, sys.stdin.readline().rstrip().split()))

for i in range(1, len(rings)):
    print('{}/{}'.format(rings[0] // math.gcd(rings[0], rings[i]), rings[i] // math.gcd(rings[0], rings[i])))
