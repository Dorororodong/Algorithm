T = int(input())

for tc in range(1, T+1):
    N = int(input())
    if N % 2:
        print('#{} {}'.format(tc, 'Odd'))

    else:
        print('#{} {}'.format(tc, 'Even'))