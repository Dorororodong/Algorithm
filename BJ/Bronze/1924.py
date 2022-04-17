cal = {1 : 31, 2 : 28, 3 : 31, 4 : 30, 5 : 31, 6 : 30, 7 : 31, 8 : 31, 9 : 30, 10 : 31, 11 : 30, 12: 31}
day = ['MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN']

import sys
x, y = map(int, sys.stdin.readline().rstrip().split())
cnt_day = y - 1

for i in range(1, x):
    cnt_day += cal[i]

print(day[cnt_day % 7])