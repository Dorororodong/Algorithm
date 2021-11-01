import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())

    if N == 0:
        print(1, 0)
    elif N == 1:
        print(0, 1)
    else:
        result = [0] * (N + 1)
        result[N] = 1
        for i in range(N, 1, -1):
            if result[i] != 0:
                result[i-1] += result[i]
                result[i-2] += result[i]
        print(result[0], result[1])

# def fibo(n):
#     if n == 0:
#         result[0] += 1
#         return
#
#     elif n == 1:
#         result[1] += 1
#         return
#
#     else:
#         fibo(n - 1)
#         fibo(n - 2)
#         return
#
# T = int(input())
# for tc in range(1, T+1):
#     result = [0, 0]
#     fibo(int(input()))
#     print(*result)