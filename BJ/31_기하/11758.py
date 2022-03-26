# 외적, 신발끈 공식
import sys
x_loc = []
y_loc = []

for _ in range(3):
    x, y = map(int, sys.stdin.readline().rstrip().split())
    x_loc.append(x)
    y_loc.append(y)

result = (x_loc[0] * y_loc[1] + x_loc[1] * y_loc[2] + x_loc[2] * y_loc[0]) - (x_loc[1] * y_loc[0] + x_loc[2] * y_loc[1] + x_loc[0] * y_loc[2])

# 0보다 크면 반시계 / 0이면 직선 / 0보다 작으면 시계 방향!
if result > 0:
    print(1)

elif result == 0:
    print(0)

else:
    print(-1)