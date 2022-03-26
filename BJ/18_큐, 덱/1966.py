# RuntimeError: deque mutated during iteration
# for문 돌 때 해당하는 list가 바뀐다면? / 많이 겪었던 문제니까 / 비교하는 곳을 잘 파악하길 [0]

import sys
from collections import deque
T = int(sys.stdin.readline().rstrip())

for _ in range(T):
    N, M = map(int, sys.stdin.readline().rstrip().split())              # N : 숫자 갯수, 알고 싶은 숫자의 idx
    idx = deque([i for i in range(N)])
    doc = deque(list(map(int, sys.stdin.readline().rstrip().split())))

    cnt = 0

    while True:
        if doc[0] == max(doc):
            cnt += 1
            doc.popleft()

            if idx.popleft() == M:
                print(cnt)
                break

        else:
            doc.append(doc.popleft())
            idx.append((idx.popleft()))