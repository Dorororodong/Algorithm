def hansoo(n):
    global cnt
    for i in range(1, n+1):
        if i <= 99:
            cnt += 1

        elif i == 1000:
            pass

        else:
            if (i // 100 - (i % 100) // 10) == ((i % 100) // 10 - i % 10):
                cnt += 1

import sys
N = int(sys.stdin.readline().rstrip())
cnt = 0

hansoo(N)

print(cnt)