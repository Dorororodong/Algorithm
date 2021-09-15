T = int(input())

for tc in range(1, T+1):
    num = list(map(int, input().split()))
    num.remove(max(num))
    num.remove(min(num))

    result = sum(num) / len(num)

    print('#{} {}'.format(tc, int(round(result,0))))