T = int(input())

for tc in range(1, T+1):
    N = int(input())

    haystack = list(int(input()) for _ in range(N))
    result = 0
    for i in haystack:
        if i > sum(haystack) // len(haystack):
            result += i - sum(haystack) // len(haystack)

    print('#{} {}'.format(tc, result))