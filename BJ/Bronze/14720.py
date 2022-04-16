import sys
N = int(sys.stdin.readline().rstrip())
milk = list(map(int, sys.stdin.readline().rstrip().split()))

cnt = 0
kind = 0

for i in milk:
    if kind % 3 == i:
        kind += 1
        cnt += 1

print(cnt)