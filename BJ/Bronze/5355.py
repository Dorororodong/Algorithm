import sys
T = int(sys.stdin.readline().rstrip())
for _ in range(1, T+1):
    mars = list(sys.stdin.readline().rstrip().split())
    num = float(mars[0])

    for i in mars[1:]:
        if i == '@':
            num *= 3
        elif i == '%':
            num += 5
        else:
            num -= 7

    print('{:.2f}'.format(num))