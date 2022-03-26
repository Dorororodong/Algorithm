import sys
import math

M, N = map(int, sys.stdin.readline().rstrip().split())

all_num = [False] * 2 + [True] * (N - 1)

for i in range(2, int(math.sqrt(N)) + 1):
    if all_num[i]:
        for j in range(2 * i, N + 1, i):
            all_num[j] = False

for k in range(M, N+1):
    if all_num[k]:
        print(k)


'''
조금 다름...!
import sys
input=sys.stdin.readline

m,n=map(int,input().split())

check=[False]*(n+1)
prime=[]
for i in range(2,n+1):
    if check[i]==False:
        if i>=m:
            prime.append(i)
        for j in range(i*i,n+1,i):
            check[j]=True

print('\n'.join(map(str,prime)))
'''