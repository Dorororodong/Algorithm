def reward(d):
    global result

    if len(set(d)) == len(d):
        if result < max(d) * 100:
            result = max(d) * 100

    else:
        for i in range(1, 7):
            if d.count(i) == 3:
                if result < 10000 + i * 1000:
                    result = 10000 + i * 1000

            elif d.count(i) == 2:
                if result < 1000 + i * 100:
                    result = 1000 + i * 100

import sys
T = int(sys.stdin.readline().rstrip())
result = 0

for _ in range(1, T+1):
    dice = list(map(int, sys.stdin.readline().rstrip().split()))
    reward(dice)

print(result)