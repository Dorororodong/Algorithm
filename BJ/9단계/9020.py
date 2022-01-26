import sys
import math

# def is_prime(n):
#     if n == 1:
#         return False
#
#     elif n == 2 or n == 3:
#         return True
#
#     else:
#         for i in range(2, int(math.sqrt(n)) + 1):
#             if n % i == 0:
#                 return False
#
#         return True

T = int(sys.stdin.readline().rstrip())

for _ in range(T):
    N = int(sys.stdin.readline().rstrip())
    numbers = [i for i in range(2, N+1)]
    result = []

    for j in range(2, int(math.sqrt(N)) + 1):
        if j in numbers:
            for k in range(2 * j, N + 1, j):
                if numbers[k]:
                    numbers[k] = 0

    for i in numbers:
        if i:
            result.append((i, N-i, abs(2 * i - N)))

    result.sort(key = lambda x : x[2])

    print(result[0][0], result[0][1])