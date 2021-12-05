T = int(input())

for tc in range(1, T+1):
    N, K = map(int, input().split())
    submit = list(map(int, input().split()))

    students = [i for i in range(1, N+1)]

    print('#{}'.format(tc), end=' ')
    for i in students:
        if i not in submit:
            print(i, end=' ')
    print()