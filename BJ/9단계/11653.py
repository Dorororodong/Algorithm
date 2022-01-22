import sys
import math

N = int(sys.stdin.readline().rstrip())

while N != 1:
    if N == 2 or N == 3:
        print(N)
        break
    else:
        for i in range(2, int(math.sqrt(N)) + 1):
            while N % i == 0:
                N //= i
                print(i)

        if i == int(math.sqrt(N)):
            print(N)
            break