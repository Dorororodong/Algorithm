import sys
N = int(sys.stdin.readline().rstrip())
nums = []
max_res = 0

for _ in range(N):
    nums.append(int(sys.stdin.readline().rstrip()))

nums.sort(reverse=True)

for i in range(N):
    if max_res < nums[i] * (i + 1):
        max_res = nums[i] * (i + 1)

print(max_res)