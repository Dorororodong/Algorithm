import sys, math
T = int(sys.stdin.readline().rstrip())

for _ in range(T):
    a, b = map(int, sys.stdin.readline().rstrip().split())
    print(math.lcm(a, b), math.gcd(a, b))