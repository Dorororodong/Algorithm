import sys
N = int(sys.stdin.readline().rstrip())
A = list(map(int, sys.stdin.readline().rstrip().split()))
B, C = map(int, sys.stdin.readline().rstrip().split())

cnt = 0

for i in range(len(A)):
    cnt += 1
    A[i] = A[i] - B

    if A[i] > 0:
        if A[i] % C != 0:
            cnt += (A[i] // C) + 1

        else:
            cnt += A[i] // C
print(cnt)

'''
import sys
N = int(sys.stdin.readline().rstrip())
A = list(map(int, sys.stdin.readline().rstrip().split()))
B, C = map(int, sys.stdin.readline().rstrip().split())

cnt = 0

for i in range(len(A)):
    if A[i] <= B:
       cnt += 1
       A[i] = 0

    else:
        cnt += 1
        A[i] = A[i] - B

for j in range(len(A)):
    if A[j] != 0:
        if A[j] % C != 0:
            cnt += (A[j] // C) + 1

        else:
            cnt += A[j] // C

print(cnt)
'''