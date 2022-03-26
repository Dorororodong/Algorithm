import sys
X = int(sys.stdin.readline().rstrip())

res = 0
cnt = 0
for i in range(1, X+1):
    res += i
    if X <= res:
        cnt += i
        break

num = res - X + 1
# 합 cnt + 1

if cnt % 2:
    print('{}/{}'.format(num, cnt + 1 - num))
else:
    print('{}/{}'.format(cnt + 1 - num, num))