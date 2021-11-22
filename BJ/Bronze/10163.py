import sys
N = int(sys.stdin.readline())
if N == 1:
    x, y, a, b = map(int, sys.stdin.readline().rstrip().split())
    print(a * b)

else:
    arr = [[0] * 1001 for _ in range(1001)]
    cnt_list = [0] * (N + 1)

    for i in range(1, N+1):
        x, y, a, b = map(int, sys.stdin.readline().rstrip().split())

        for j in range(x, x+a):
            for k in range(y, y+b):
                arr[j][k] = i


    for k in range(1001):
        for l in range(1001):
            if arr[k][l] != 0:
                cnt_list[arr[k][l]] += 1

    for m in cnt_list[1:]:
        print(m)
