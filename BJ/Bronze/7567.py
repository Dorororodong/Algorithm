import sys
bowl = sys.stdin.readline().rstrip()
height = 10

for i in range(1, len(bowl)):
    if bowl[i] == bowl[i-1]:
        height += 5

    else:
        height += 10

print(height)