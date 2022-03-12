import sys
S = int(sys.stdin.readline().rstrip())
n = 1

while n * (n + 1) / 2 < S:
    n += 1

if S == n * (n + 1) / 2:
    print(n)

else:
    print(n - 1)
