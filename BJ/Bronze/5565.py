import sys
total = int(sys.stdin.readline().rstrip())

yes_read = 0

for _ in range(9):
    yes_read += int(sys.stdin.readline().rstrip())

print(total - yes_read)