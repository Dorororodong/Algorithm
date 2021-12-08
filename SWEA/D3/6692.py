T = int(input())

for tc in range(1, T+1):
    N = int(input())
    income = 0
    for _ in range(N):
        p, x = map(float, input().split())
        income += p * x
    print('#{} {}'.format(tc, income))