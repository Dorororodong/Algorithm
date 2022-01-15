import sys
T = int(sys.stdin.readline().rstrip())

result = [0, 0, 0]

while T >= 10:
    if T >= 300:
        result[0] += T // 300
        T %= 300

    elif T >= 60:
        result[1] += T // 60
        T %= 60

    else:
        result[2] += T // 10
        T %= 10

if T == 0:
    print(*result)

else:
    print(-1)