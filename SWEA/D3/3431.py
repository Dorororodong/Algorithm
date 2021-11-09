T = int(input())

for tc in range(1, T+1):
    L, U, X = map(int, input().split())

    if X > U:
        print('#{} {}'.format(tc, -1))
    elif L <= X <= U:
        print('#{} {}'.format(tc, 0))
    else:
        print('#{} {}'.format(tc, L-X))