T = int(input())

for tc in range(1, T+1):
    N, A, B = map(int, input().split())
    if A + B > N:
        print('#{} {} {}'.format(tc, min(A, B), A + B - N))
    else:
        print('#{} {} {}'.format(tc, min(A, B), 0))