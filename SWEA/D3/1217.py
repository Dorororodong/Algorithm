def recursion(n, m):
    if m == 1:
        return n

    else:
        return n * recursion(n, m-1)

for _ in range(1, 11):
    tc = int(input())
    N, M = map(int, input().split())

    result = recursion(N, M)
    print('#{} {}'.format(tc, result))