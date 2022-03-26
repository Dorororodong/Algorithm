import math

T = int(input())

for tc in range(1, T+1):
    a, b = map(int, input().split())

    print(math.lcm(a, b))


'''
def gcd(m, n):
    if n != 0:
        return gcd(n, m % n)
    return m

T = int(input())

for tc in range(1, T+1):
    a, b = map(int, input().split())

    print(int(a * b / gcd(a, b)))
'''