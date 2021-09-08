T = int(input())

for tc in range(1, T+1):
    calendar = input()
    if len(calendar) != 8:
        print(-1)
    else:
        if 0 < int(calendar[4:6]) < 13:
            if int(calendar[4:6]) == 4 or int(calendar[4:6]) == 6 or int(calendar[4:6]) == 9 or int(calendar[4:6]) == 11:
                if int(calendar[6:8]) > 30 or int(calendar[6:8]) == 0:
                    print(-1)
                else:
                    print('#{} {}/{}/{}'.format(tc, calendar[0:4], calendar[4:6], calendar[6:8]))

            elif int(calendar[4:6]) == 2:
                if int(calendar[6:8]) > 28 or int(calendar[6:8]) == 0:
                    print(-1)
                else:
                    print('#{} {}/{}/{}'.format(tc, calendar[0:4], calendar[4:6], calendar[6:8]))

            else:
                if int(calendar[6:8]) > 31 or int(calendar[6:8]) == 0:
                    print(-1)
                else:
                    print('#{} {}/{}/{}'.format(tc, calendar[0:4], calendar[4:6], calendar[6:8]))
        else:
            print(-1)