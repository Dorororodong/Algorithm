T = int(input())

for tc in range(1, T+1):
    a, b = map(int, input().split())

    if a + b == 24:
        print('#{} {}'.format(tc, 0))

    elif a + b < 24:
        print('#{} {}'.format(tc, a + b))

    else:
        print('#{} {}'.format(tc, a + b - 24))