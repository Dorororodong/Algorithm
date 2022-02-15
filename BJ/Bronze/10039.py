import sys
total = 0
for _ in range(5):
    n = int(sys.stdin.readline().rstrip())

    if n < 40:
        total += 40

    else:
        total += n

print(total // 5)