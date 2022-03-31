import sys
n = int(sys.stdin.readline().rstrip())
stack = []
seq = [int(sys.stdin.readline().rstrip()) for _ in range(n)]

num = 1
idx = 0
res = []

while idx != n:
    if num > n + 1:
        break

    if stack:
        if stack[-1] != seq[idx]:
            stack.append(num)
            res.append('+')
            num += 1

        else:
            stack.pop()
            res.append('-')
            idx += 1

    else:
        stack.append(num)
        res.append('+')
        num += 1

if num > n + 1:
    print('NO')

else:
    for i in res:
        print(i)

'''
import sys
input = sys.stdin.readline

n = int(input())

stack = []
ans = []
count = 1
for _ in range(n):
    t = int(input())
    while count <= t:
        stack.append(count)
        ans.append('+')
        count+=1
    if stack[-1] == t:
        stack.pop()
        ans.append('-')
    else:
        print('NO')
        exit(0)

print('\n'.join(ans))
'''