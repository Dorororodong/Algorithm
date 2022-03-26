while True:
    num = list(map(int, input().split()))

    max_num = max(num)

    num.remove(max_num)

    if max_num == 0:
        break

    else:
        if max_num ** 2 == num[0] ** 2 + num[1] ** 2:
            print('right')

        else:
            print('wrong')