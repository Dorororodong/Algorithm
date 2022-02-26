import sys
dice = list(map(int, sys.stdin.readline().rstrip().split()))

if len(set(dice)) == len(dice):
    print(max(dice) * 100)

else:
    for i in range(1, 7):
        if dice.count(i) == 3:
            print(10000 + i * 1000)

        elif dice.count(i) == 2:
            print(1000 + i * 100)