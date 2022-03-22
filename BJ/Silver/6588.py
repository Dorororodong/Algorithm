def is_prime(n):
    for j in range(2, int(math.sqrt(n)) + 1):
        if n % j == 0:
            return False

    return True

import sys, math
Eratosthenes = [False, False] + [True] * 999999
primes = []

for i in range(2, 1000001):
    if Eratosthenes[i]:
        primes.append(i)

        for j in range(2 * i, 1000001, i):
            Eratosthenes[j] = False

while True:
    n = int(sys.stdin.readline().rstrip())

    if n == 0:
        break

    else:
        for i in primes:
            another_n = n - i

            if is_prime(another_n):
                print('{} = {} + {}'.format(n, i, another_n))
                break

'''
import sys
rl = sys.stdin.readline
wr = sys.stdout.write

nums = [1] * 1000001
nums[0] = nums[1] = 0

for i in range(2, 1000001):
    if nums[i]:
        ith = i + i
        
        while ith < 1000001:
            nums[ith] = 0
            ith += i

while True:
    n = int(rl())
    
    if n == 0:
        break
        
    for i in range(3, 500001, 2):
        if nums[i] and nums[n - i]:
            wr(f'{n} = {i} + {n - i}\n')
            break
'''