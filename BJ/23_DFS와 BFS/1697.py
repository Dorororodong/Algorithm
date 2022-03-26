def BFS(n, k):
    Q = deque()
    Q.append((n, k))

    while Q:
        n, k = Q.popleft()

        if n == k:
            print(scope[n])
            break

        for nn in (n - 1, n + 1, 2 * n):
            # 전이든, 동시든 시간이 같다는 것은 이든저든 방법이 있는거니까 바꿔줄 필요가 없음(아무리 좋아도 같은 시각에 간다는 거니까)
            if 0 <= nn <= 100000 and scope[nn] == 0:
                scope[nn] = scope[n] + 1
                Q.append((nn, k))

import sys
from collections import deque
N, K = map(int, sys.stdin.readline().rstrip().split())
scope = [0] * 100001

BFS(N, K)

# Thanks to : https://wook-2124.tistory.com/273