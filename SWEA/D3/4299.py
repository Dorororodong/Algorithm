T = int(input())

for tc in range(1, T+1):
    D, H, M = map(int, input().split())

    if D < 11:
        print('#{} {}'.format(tc, -1))

    elif D == 11:
        if H < 11:
            print('#{} {}'.format(tc, -1))

        elif H == 11:
            if M < 11:
                print('#{} {}'.format(tc, -1))

            elif M == 11:
                print('#{} {}'.format(tc, 0))

            else:
                print('#{} {}'.format(tc, 1440 * (D - 11) + 60 * (H - 11) + (M - 11)))

        else:
            print('#{} {}'.format(tc, 1440 * (D - 11) + 60 * (H - 11) + (M - 11)))

    else:
        print('#{} {}'.format(tc, 1440 * (D - 11) + 60 * (H - 11) + (M - 11)))