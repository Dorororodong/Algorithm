import sys
N = int(sys.stdin.readline().rstrip())
switch = list(map(int, sys.stdin.readline().rstrip().split()))
students = int(sys.stdin.readline().rstrip())

switch = [0] + switch

for _ in range(students):
    gender, num = map(int, sys.stdin.readline().rstrip().split())

    if gender == 1:
        for i in range(num, N+1, num):
            if switch[i] == 0:
                switch[i] = 1

            else:
                switch[i] = 0

    else:
        if switch[num] == 0:
            switch[num] = 1

        else:
            switch[num] = 0

        cnt = 1

        while 1 <= num - cnt and num + cnt <= N:
            if switch[num - cnt] == switch[num + cnt]:
                if switch[num - cnt] == 0:
                    switch[num - cnt] = 1
                    switch[num + cnt] = 1
                    cnt += 1

                else:
                    switch[num - cnt] = 0
                    switch[num + cnt] = 0
                    cnt += 1
            else:
                break

switch = switch[1:]

for i in range(len(switch) // 21 + 1):
    print(' '.join(map(str, switch[20 * i : 20 * (i+1)])))