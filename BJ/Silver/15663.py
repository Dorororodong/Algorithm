import sys
from itertools import permutations
N, M = map(int, sys.stdin.readline().rstrip().split())
nums = list(map(int, sys.stdin.readline().rstrip().split()))

ans = list(permutations(nums, M))
real_ans = sorted(list(set(ans)))

for i in real_ans:
    print(*i)

'''
# 중복된 순열은 출력이 안되게! (now!)

import sys
input = sys.stdin.readline

def nm(x):
    if x == m:
        print(' '.join(tmp))
        return
    
    now = 0
    for i in range(n):
        if not visit[i] and now != db[i]:
            visit[i] = 1
            tmp.append(db[i])
            now = db[i]
            nm(x + 1)
            visit[i] = 0
            tmp.pop()

n, m = map(int, input().split())
db = input().split()
db.sort(key = lambda x : int(x))
visit = [0] * n
tmp = []

nm(0)
'''