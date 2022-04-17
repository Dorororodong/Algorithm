import sys
N, M = map(int, sys.stdin.readline().rstrip().split())
A = list(map(int, sys.stdin.readline().rstrip().split()))
B = list(map(int, sys.stdin.readline().rstrip().split()))

a = 0
b = 0

res = []

while a != N or b != M:
    if a == N:
        res.append(B[b])
        b += 1

    elif b == M:
        res.append(A[a])
        a += 1

    else:
        if A[a] < B[b]:
            res.append(A[a])
            a += 1

        else:
            res.append(B[b])
            b += 1

print(' '.join(map(str, res)))
# print(*res)

'''
import sys
N, M = map(int, sys.stdin.readline().rstrip().split())
A = list(map(int, sys.stdin.readline().rstrip().split()))
B = list(map(int, sys.stdin.readline().rstrip().split()))

print(' '.join(map(str, sorted(A + B))))
# print(*sorted(A + B))
'''