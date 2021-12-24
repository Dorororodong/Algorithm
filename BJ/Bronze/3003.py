import sys

chess = list(map(int, sys.stdin.readline().rstrip().split()))

for i in range(6):
    if i <= 1:
        chess[i] = 1 - chess[i]
    elif i <= 4:
        chess[i] = 2 - chess[i]
    else:
        chess[i] = 8 - chess[i]

print(*chess)