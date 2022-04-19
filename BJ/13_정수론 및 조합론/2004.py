def find_two(num):
    cnt = 0
    while num:
        num //= 2
        cnt += num

    return cnt

# 25! : 한번 거르면 5,10,15,20,25 털림 (+5) / 근데 25는 한번 더 털려야 함(+1) / 그 후엔 몫이 0! (의미없음)
def find_five(num):
    cnt = 0
    while num:
        num //= 5
        cnt += num

    return cnt

import sys
n, m = map(int, sys.stdin.readline().rstrip().split())

print(min(find_two(n) - find_two(m) - find_two(n-m), find_five(n) - find_five(m) - find_five(n-m)))