T = int(input())

for tc in range(1, T+1):
    scores = list(map(int, input().split()))

    for i in range(5):
        if scores[i] < 40:
            scores[i] = 40

    print('#{} {}'.format(tc, sum(scores) // 5))