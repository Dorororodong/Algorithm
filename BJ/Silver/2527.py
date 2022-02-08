import sys
for _ in range(4):
    loc = list(map(int, sys.stdin.readline().rstrip().split()))

    if (loc[2] < loc[4]) or (loc[6] < loc[0]) or (loc[3] < loc[5]) or (loc[7] < loc[1]):
        print('d')

    elif (loc[0] == loc[6] and loc[1] == loc[7]) or (loc[2] == loc[4] and loc[3] == loc[5]) or (loc[0] == loc[6] and loc[3] == loc[5]) or (loc[1] == loc[7] and loc[2] == loc[4]):
        print('c')

    elif (loc[1] == loc[7] and (loc[0] < loc[6] and loc[4] < loc[2])) or (loc[0] == loc[6] and (loc[1] < loc[7] and loc[5] < loc[3])) or (loc[3] == loc[5] and (loc[4] < loc[2] and loc[0] < loc[6])) or (loc[2] == loc[4] and (loc[1] < loc[7] and loc[5] < loc[3])):
        print('b')

    else:
        print('a')