import sys

while True:
    res = 2
    N = sys.stdin.readline().rstrip()

    if N == '0':
        break

    else:
        n = len(N)
        res += n - 1

        for i in range(n):
            if N[i] == '0':
                res += 4

            elif N[i] == '1':
                res += 2

            else:
                res += 3

        print(res)