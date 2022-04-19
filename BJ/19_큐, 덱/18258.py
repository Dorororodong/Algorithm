import sys
from collections import deque
N = int(sys.stdin.readline())
result = deque()
for _ in range(N):
    num = sys.stdin.readline().split()

    if num[0] == 'push':
        result.append(num[1])

    elif num[0] == 'pop':
        if len(result) != 0:
            print(result.popleft())

        else:
            print(-1)

    elif num[0] == 'size':
        print(len(result))

    elif num[0] == 'empty':
        if len(result) != 0:
            print(0)

        else:
            print(1)

    elif num[0] == 'front':
        if len(result) != 0:
            print(result[0])

        else:
            print(-1)

    elif num[0] == 'back':
        if len(result) != 0:
            print(result[-1])

        else:
            print(-1)