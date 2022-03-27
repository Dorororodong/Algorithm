import sys
N, R = map(int, sys.stdin.readline().rstrip().split())
comback_volunteers = list(map(int, sys.stdin.readline().rstrip().split()))

volunteers = [i for i in range(1, N + 1)]

res = set(volunteers) - set(comback_volunteers)

if res:
    print(" ".join(map(str, sorted(list(res)))))

else:
    print("*")

'''
# 집합으로 교집합 가능!
a,b=map(int,input().split())
k=set(i+1 for i in range(a))
d=set(map(int,input().split()))
if a==b:print('*')
else:print(*k^d)
'''