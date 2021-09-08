T = int(input())

for tc in range(1, T+1):
    num = list(map(int, input().split()))

    print('#{} {}'.format(tc, max(num)))