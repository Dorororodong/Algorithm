T = int(input())

for tc in range(1, T+1):
    N = int(input())
    income = list(map(int, input().split()))
    cnt = 0
    for i in range(N):
        if income[i] <= (sum(income) / N):
            cnt += 1

    print('#{} {}'.format(tc, cnt))
