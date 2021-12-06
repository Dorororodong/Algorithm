T = int(input())

for tc in range(1, T+1):
    N, K = map(int, input().split())
    scores = sorted(list(map(int, input().split())), reverse=True)

    print('#{} {}'.format(tc, sum(scores[:K])))
