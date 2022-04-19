import sys
N, M = map(int, sys.stdin.readline().rstrip().split())
A = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(N)]
M, K = map(int, sys.stdin.readline().rstrip().split())
B = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(M)]
C = [[0] * K for _ in range(N)]

# 행
for i in range(N):
    # 열
    for j in range(K):
        # 공통 (계산이 가능하게 해주는 숫자)
        for k in range(M):
            C[i][j] += A[i][k] * B[k][j]

for l in C:
    print(*l)

'''
import numpy as np
import sys
N, M1 = map(int, sys.stdin.readline().rstrip().split())
A = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(N)]
M2, K = map(int, sys.stdin.readline().rstrip().split())
B = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(M2)]
A_arr = np.array(A)
B_arr = np.array(B)
result = np.dot(A_arr, B_arr)
for i in result:
    print(*i)
'''