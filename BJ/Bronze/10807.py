import sys
N = int(sys.stdin.readline().rstrip())
int_list = list(map(int, sys.stdin.readline().rstrip().split()))
v = int(sys.stdin.readline().rstrip())

print(int_list.count(v))

'''
import sys
N = int(sys.stdin.readline().rstrip())
int_list = list(map(int, sys.stdin.readline().rstrip().split()))
v = int(sys.stdin.readline().rstrip())

cnt = 0
for i in range(N):
    if int_list[i] == v:
        cnt += 1

print(cnt)
'''