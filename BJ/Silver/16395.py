# 내가 알던 수학식을 코드로! (dp로 미리 설정을 할 때는 주어진 범위를 잘 보도록!)
import sys
pascal = [[1 for _ in range(i)] for i in range(1, 31)]

for i in range(2, 30):
    for j in range(1, i):
        pascal[i][j] = pascal[i-1][j-1] + pascal[i-1][j]

n, k = map(int, sys.stdin.readline().rstrip().split())
print(pascal[n-1][k-1])

'''
import sys, math
n, k = map(int, sys.stdin.readline().rstrip().split())

if k == 1 or k == n:
    print(1)

else:
    print(math.factorial(n-1) // math.factorial(k-1) // math.factorial(n - k))
'''