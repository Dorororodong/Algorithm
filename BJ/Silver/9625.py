import sys
K = int(sys.stdin.readline().rstrip())

dp_A = [0] * (K + 1)
dp_B = [0] * (K + 1)
dp_B[1] = 1

if K == 1:
    print(dp_A[1], dp_B[1])

else:
    for i in range(2, K + 1):
        dp_A[i] = dp_B[i-1]
        dp_B[i] = dp_A[i-1] + dp_B[i-1]

    print(dp_A[K], dp_B[K])