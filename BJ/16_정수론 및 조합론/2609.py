import math

a, b = map(int, input().split())

print(math.gcd(a, b))
print(math.lcm(a, b))


'''
#유클리드 호제법
def GCD(M, N): # 최대공약수
    if N == 0:
        return M
    return GCD(N, M % N)
    
M, N = map(int, input().split())

print(GCD(M, N))
#최소공배수
print(int(M * N / GCD(M, N)))
'''