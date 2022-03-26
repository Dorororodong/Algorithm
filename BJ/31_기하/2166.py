import sys
N = int(sys.stdin.readline().rstrip())
x_loc = []
y_loc = []

for _ in range(N):
    x, y = map(int, sys.stdin.readline().rstrip().split())
    x_loc.append(x)
    y_loc.append(y)

x_loc.append(x_loc[0])
y_loc.append(y_loc[0])
length = len(x_loc)
first_res = 0
second_res = 0

for i in range(length-1):
    first_res += x_loc[:-1][i] * y_loc[1:][i]
    second_res += x_loc[1:][i] * y_loc[:-1][i]

ans = 0.5 * abs(first_res - second_res)

print(round(ans, 1))