import sys

while True:
    n = int(sys.stdin.readline().rstrip())
    measure = 1
    measure_list = [1]

    if n == -1:
        break

    else:
        for i in range(2, n):
            if n % i == 0:
                measure += i
                measure_list.append(i)

        if n == measure:
            print('{} {} {}'.format(n, '=', " + ".join(map(str, measure_list))))

        else:
            print('{} {}'.format(n, 'is NOT perfect.'))