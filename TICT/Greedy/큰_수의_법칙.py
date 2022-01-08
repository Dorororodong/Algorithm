'''
5 8 3
2 4 5 4 6
'''

import sys
sys.stdin = open('input.txt')

N, M, K = map(int, input().split())
numbers = list(map(int, input().split()))

numbers.sort()

result = 0

while M > 0:

    for _ in range(K):
        result += numbers[-1]
        M -= 1
        if M == 0:
            break

    if M == 0:
        break
    result += numbers[-2]
    M -= 1

print(result)

# 46