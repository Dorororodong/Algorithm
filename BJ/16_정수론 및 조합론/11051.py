import sys, math
N, K = map(int, sys.stdin.readline().rstrip().split())
print(math.factorial(N) // math.factorial(N-K) // math.factorial(K) % 10007)