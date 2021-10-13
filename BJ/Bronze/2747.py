import sys

n = int(sys.stdin.readline())

a, b = 0, 1

while n > 0:
    a, b = b, a + b
    n -= 1

print(a)

'''
import sys

def fibo(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibo(n-1) + fibo(n-2)

print(fibo(int(sys.stdin.readline())))
'''