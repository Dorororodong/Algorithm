import sys
from collections import defaultdict
N, M = map(int, sys.stdin.readline().rstrip().split())

all_group = defaultdict(list)

for _ in range(N):
    group = sys.stdin.readline().rstrip()
    n = int(sys.stdin.readline().rstrip())

    for _ in range(n):
        all_group[group].append(sys.stdin.readline().rstrip())

all_members = list(all_group.values())

for _ in range(M):
    who = sys.stdin.readline().rstrip()
    m = int(sys.stdin.readline().rstrip())

    if m == 0:
        print('\n'.join(sorted(all_group[who])))

    else:
        for i in range(N):
            if who in all_members[i]:
                print(list(all_group)[i])
                break