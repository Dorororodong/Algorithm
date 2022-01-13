'''
a1
'''

import sys
sys.stdin = open('input.txt')

loc = input()

cnt = 0

row = int(loc[1]) - 1
col = ord(loc[0]) - 97

can_move = [(-1, -2), (1, -2), (-1, 2), (1, 2), (-2, -1), (-2, 1), (2, -1), (2, 1)]

for i in can_move:
    n_row = row + i[0]
    n_col = col + i[1]

    if 0 <= n_row < 8 and 0 <= n_col < 8:
        cnt += 1

# print(row, col)
print(cnt)