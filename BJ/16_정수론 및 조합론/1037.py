import sys

N = int(sys.stdin.readline().rstrip())

divisor = list(map(int, sys.stdin.readline().rstrip().split()))

if len(divisor) == 1:
    print(divisor[0] ** 2)

else:
    print(max(divisor) * min(divisor))