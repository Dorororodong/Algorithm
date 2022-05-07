import sys
N, M = map(int, sys.stdin.readline().rstrip().split())
nums = list(map(int, sys.stdin.readline().rstrip().split()))

cnt = 0
s = 0
e = 1

while e <= N and s <= e:
    sum_nums = sum(nums[s:e])

    if sum_nums == M:
        cnt += 1
        s += 1

    elif sum_nums < M:
        e += 1

    else:
        s += 1

print(cnt)

'''
n, target = map(int, input().split())
arr = list(map(int, input().split()))

s = 0
e = 0
sum_arr = arr[0]
cnt = 0

while True:    
    if sum_arr < target:
        e += 1
        
        if e == n:
            break
            
        sum_arr += arr[e]
        
    elif sum_arr >= target:
    
        if sum_arr == target:
            cnt += 1
            
        sum_arr -= arr[s]
        s += 1

print(cnt)
'''