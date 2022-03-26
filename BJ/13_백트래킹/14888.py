def cal(dep, res, sum, sub, mul, div):
    global max_res
    global min_res

    if dep == N:
        max_res = max(max_res, res)
        min_res = min(min_res, res)
        return

    if sum > 0:
        cal(dep + 1, res + nums[dep], sum - 1, sub, mul, div)

    if sub > 0:
        cal(dep + 1, res - nums[dep], sum, sub - 1, mul, div)

    if mul > 0:
        cal(dep + 1, res * nums[dep], sum, sub, mul - 1, div)

    if div > 0:
        cal(dep + 1, int(res / nums[dep]), sum, sub, mul, div - 1)

import sys
N = int(sys.stdin.readline().rstrip())
nums = list(map(int, sys.stdin.readline().rstrip().split()))
oper = list(map(int, sys.stdin.readline().rstrip().split()))

max_res = -987654321
min_res = 987654321

cal(1, nums[0], oper[0], oper[1], oper[2], oper[3])

print(max_res)
print(min_res)

# Thanks to : https://velog.io/@kimdukbae/BOJ-14888-%EC%97%B0%EC%82%B0%EC%9E%90-%EB%81%BC%EC%9B%8C%EB%84%A3%EA%B8%B0-Python

'''
반면교사
def cal(res, idx):
    global max_res
    global min_res

    if idx == N-1:
        if max_res < res:
            max_res = res

        if min_res > res:
            min_res = res
            return

    for i in range(idx + 1, N):
        nex_num = nums[i]

        for j in range(4):
            if oper[j] > 0:
                if j == 0:
                    oper[j] -= 1
                    cal(res + nex_num, idx+1)
                    oper[j] += 1

                elif j == 1:
                    oper[j] -= 1
                    cal(res - nex_num, idx+1)
                    oper[j] += 1

                elif j == 2:
                    oper[j] -= 1
                    cal(res * nex_num, idx+1)
                    oper[j] += 1

                else:
                    oper[j] -= 1
                    if res > 0:
                        cal(res // nex_num, idx + 1)
                        oper[j] += 1

                    else:
                        cal(-(-res // nex_num), idx + 1)
                        oper[j] += 1

import sys
N = int(sys.stdin.readline().rstrip())
nums = list(map(int, sys.stdin.readline().rstrip().split()))
oper = list(map(int, sys.stdin.readline().rstrip().split()))    # 덧셈, 뺄셈, 곱셈, 나눗셈

res = nums[0]
max_res = 0
min_res = 987654321
cal(res, 0)

print(max_res)
print(min_res)
'''