from collections import deque
import sys

N = int(sys.stdin.readline().rstrip())
Q = deque()

for _ in range(N):
    que = sys.stdin.readline().rstrip().split()

    if que[0] == 'push':
        Q.append(que[1])

    elif que[0] == 'pop':
        if len(Q) == 0:
            print(-1)

        else:
            print(Q.popleft())

    elif que[0] == 'size':
        print(len(Q))

    elif que[0] == 'empty':
        if len(Q) == 0:
            print(1)

        else:
            print(0)

    elif que[0] == 'front':
        if len(Q) == 0:
            print(-1)

        else:
            print(Q[0])

    else:
        if len(Q) == 0:
            print(-1)

        else:
            print(Q[-1])
