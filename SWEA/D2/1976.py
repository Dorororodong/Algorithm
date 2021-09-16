T = int(input())

for tc in range(1, T+1):
    h1, m1, h2, m2 = map(int, input().split())

    if m1 + m2 >= 60:
        if h1 + h2 > 12:
            print('#{} {} {}'.format(tc, h1 + h2 + 1 -12, m1 + m2 -60))
        else:
            print('#{} {} {}'.format(tc, h1 + h2 + 1, m1 + m2 -60))
    else:
        if h1 + h2 > 12:
            print('#{} {} {}'.format(tc, h1 + h2 - 12, m1 + m2))
        else:
            print('#{} {} {}'.format(tc, h1 + h2, m1 + m2))