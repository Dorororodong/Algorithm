# while문과 for문의 콜라보?!
# idx 생각!
# deque가 append/pop을 조금이라도 더 빠르게!
# while문에 조건 2개도 가능!

# 796ms
import sys
from collections import deque
N = int(sys.stdin.readline().rstrip())
nums = list(map(int, sys.stdin.readline().rstrip().split()))

res = [-1] * N
stack = deque()

for i in range(N):
    while stack and stack[-1][0] < nums[i]:
        num, idx = stack.pop()
        res[idx] = nums[i]

    stack.append([nums[i], i])

print(*res)


# 664ms
import sys
N = int(sys.stdin.readline().rstrip())
nums = list(map(int, sys.stdin.readline().rstrip().split()))

res = [-1] * N
stack = [(nums[0], 0)]

for i in range(1, N):
    if nums[i] > stack[-1][0]:
        while stack and stack[-1][0] < nums[i]:
            num = stack.pop()
            res[num[1]] = nums[i]

        stack.append((nums[i], i))

    else:
        stack.append((nums[i], i))

print(*res)


'''
import sys
n = int(input())
data = list(map(int, sys.stdin.readline().split()))
ans = [-1]*n
stack = []

stack.append(0)
for i in range(1, n):
    while stack and data[stack[-1]] < data[i]:
        ans[stack.pop()] = data[i]
    stack.append(i)
print(' '.join(map(str, ans)))
'''