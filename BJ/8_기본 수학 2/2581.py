import sys
import math

def discriminate_prime_num(n):
    global prime_num
    global min_prime_num

    if n == 1:
        return

    elif n == 2 or n == 3:
        prime_num += n
        if min_prime_num == -1:
            min_prime_num = n

    else:
        for j in range(2, int(math.sqrt(n))+1):
            if n % j == 0:
                return
        prime_num += n
        if min_prime_num == -1:
            min_prime_num = n

M = int(sys.stdin.readline().rstrip())
N = int(sys.stdin.readline().rstrip())

prime_num = 0
min_prime_num = -1

for i in range(M, N+1):
    discriminate_prime_num(i)

if prime_num == 0:
    print(min_prime_num)

else:
    print(prime_num)
    print(min_prime_num)
