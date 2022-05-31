import sys

while True:
    N = int(sys.stdin.readline().rstrip())

    if N == -1:
        break

    else:
        mile = 0
        speed = [0]
        time = [0]

        for _ in range(N):
            a, b = map(int, sys.stdin.readline().rstrip().split())

            speed.append(a)
            time.append(b)

        for i in range(1, N + 1):
            mile += speed[i] * (time[i] - time[i-1])

        print(mile, 'miles')