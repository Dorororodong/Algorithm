T = int(input())

for tc in range(1, T+1):
    N = int(input())

    print('#{}'.format(tc), end=' ')

    for _ in range(N):
        print('{}{}{}'.format(1, '/', N), end=' ')
    print()