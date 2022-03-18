import sys
N = int(sys.stdin.readline().rstrip())

max_cnt = -1
res = []

for i in range(1, N + 1):
    nums = [N, i]
    cnt = 2

    while True:
        if nums[-1] >= 0:
            nums.append(nums[-2] - nums[-1])
            cnt += 1

        else:
            nums.pop()
            cnt -= 1
            break

    if max_cnt < cnt:
        max_cnt = cnt
        res = nums

print(max_cnt)
print(*res)
