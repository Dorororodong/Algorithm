import sys
arr = [[0] * 100 for _ in range(100)]
result = 0
for _ in range(4):
    x, y, a, b = map(int, sys.stdin.readline().rstrip().split())

    for i in range(x, a):
        for j in range(y, b):
            arr[i][j] = 1

for i in range(100):
    for j in range(100):
        if arr[i][j] == 1:
            result += 1

print(result)