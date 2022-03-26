import sys
A, B, N = map(int, sys.stdin.readline().rstrip().split())

A %= B

for _ in range(N-1):
    A = (A * 10) % B

print((A * 10) // B)

# 참고 : https://blex.me/@mildsalmon/%EB%B0%B1%EC%A4%80-1312%EB%B2%88-%EC%86%8C%EC%88%98