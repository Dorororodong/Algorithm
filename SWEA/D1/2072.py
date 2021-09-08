T = int(input())

for tc in range(1, T+1):
    num = list(map(int, input().split()))
    sum = 0
    for i in num:
        if i % 2 == 1:
            sum += i
    print('#{} {}'.format(tc, sum))