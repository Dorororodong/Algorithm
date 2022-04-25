import sys, math
M = int(sys.stdin.readline().rstrip())
N = int(sys.stdin.readline().rstrip())

res = []
total = -1

for i in range(M, N + 1):
    if int(math.sqrt(i)) == math.sqrt(i):
        res.append(i)
        total += i

if total == -1:
    print(total)

else:
    print(total + 1)
    print(res[0])