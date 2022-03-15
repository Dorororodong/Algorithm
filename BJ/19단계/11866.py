import sys
from collections import deque
N, K = map(int, sys.stdin.readline().rstrip().split())
josephus = deque(i for i in range(1, N+1))

print('<', end='')

while josephus:
    for _ in range(K):
        josephus.append(josephus.popleft())

    if len(josephus) > 1:
        print(josephus.pop(), end='')
        print(', ', end='')

    else:
        print(josephus.pop(), end='')

print('>')