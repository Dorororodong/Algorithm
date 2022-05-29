import sys
from collections import deque
T = int(sys.stdin.readline().rstrip())

for _ in range(T):
    p = sys.stdin.readline().rstrip()
    n = int(sys.stdin.readline().rstrip())
    arr = sys.stdin.readline().rstrip()[1:-1].split(',')
    queue = deque(arr)

    rev, flag = 0, True

    if n == 0:
        queue = []

    for i in p:
        if i == 'R':
            rev += 1

        else:
            if len(queue) < 1:
                flag = False
                print('error')
                break

            else:
                if rev % 2:
                    queue.pop()

                else:
                    queue.popleft()

    if flag:
        if rev % 2:
            queue.reverse()
            print('[' + ','.join(queue) + ']')

        else:
            print('[' + ','.join(queue) + ']')