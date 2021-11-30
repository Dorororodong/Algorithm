import sys

N = int(sys.stdin.readline().rstrip())

N_factorial = 1

for i in range(2, N+1):
    N_factorial *= i

cnt = 0
for j in str(N_factorial)[::-1]:
    if j == '0':
       cnt += 1
    else:
        break

print(cnt)