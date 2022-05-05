import sys
N = list(map(int, sys.stdin.readline().rstrip()))

nums = [0] * 10
num_six_nine = 0

for i in N:
    if i != 6 and i != 9:
        nums[i] += 1

    else:
        num_six_nine += 1

print(max(max(nums), (num_six_nine // 2 + num_six_nine % 2)))