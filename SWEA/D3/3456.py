T = int(input())

for tc in range(1, T+1):
    rectangle = list(map(int, input().split()))
    for i in rectangle:
        if rectangle.count(i) == 1 or rectangle.count(i) == 3:
            print('#{} {}'.format(tc, i))
            break