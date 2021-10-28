'''
N 개의 숫자로 구성된 숫자열 Ai (i=1~N) 와 M 개의 숫자로 구성된 숫자열 Bj (j=1~M) 가 있다.

N 과 M은 3 이상 20 이하이다.
'''

import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    # print(N, M)
    # print(A)
    # print(B)

    max_value = 0

    if N <= M:
        for i in range(M-N+1):
            result = 0
            for j in range(N):
                result += (A[j] * B[i+j])
            if result > max_value:
                max_value = result

    else:
        for i in range(N-M+1):
            result = 0
            for j in range(M):
                result += (A[i + j] * B[j])
            if result > max_value:
                max_value = result

    print('#{} {}'.format(tc, max_value))

#1 30
#2 63
#3 140
#4 181
#5 63
#6 58
#7 22
#8 120
#9 96
#10 70