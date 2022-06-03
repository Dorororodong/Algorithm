import sys
max_res = -1
max_r, max_c = -1, -1

grid = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(9)]

for i in range(9):
    for j in range(9):
        if grid[i][j] > max_res:
            max_res = grid[i][j]
            max_r, max_c = i, j

print(max_res)
print(max_r + 1, max_c + 1)