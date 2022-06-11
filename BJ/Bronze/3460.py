import sys
T = int(sys.stdin.readline().rstrip())

for _ in range(T):
    n = int(sys.stdin.readline().rstrip())

    bin_num = bin(n)[2:][::-1]

    num = 0

    for i in bin_num:
        if i == '1':
            print(num, end=' ')

        num += 1