import sys
N = int(sys.stdin.readline().rstrip())
cnt = 0
nums = 666

while True:
    if '666' in str(nums):
        cnt += 1

    if N == cnt:
        print(nums)
        break

    nums += 1