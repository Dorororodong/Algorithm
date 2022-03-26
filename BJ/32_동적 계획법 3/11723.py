# 비트마스킹? 배우긴 했는데... 가능?

import sys
M = int(sys.stdin.readline().rstrip())
S = set()

for _ in range(M):
    x = sys.stdin.readline().rstrip().split()

    if len(x) == 1:
        if x[0] == 'all':
            S = set([i for i in range(1, 21)])

        else:
            S = set()

    else:
        command, target = x[0], int(x[1])
        if command == 'add':
            S.add(target)

        elif command == 'remove':
            S.discard(target)

        elif command == 'check':
            if target in S:
                print(1)
            else:
                print(0)

        else:
            if target in S:
                S.discard(target)
            else:
                S.add(target)