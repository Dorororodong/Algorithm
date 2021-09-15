T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())

    arr = [list(map(int, input().split())) for _ in range(N)]
    
    die_num = []

    for i in range(N-M+1):
        for j in range(N-M+1):
            result = 0
            for k in range(M):
                for l in range(M):
                    result += arr[i+k][j+l]
            die_num.append(result)

    print('#{} {}'.format(tc, max(die_num)))