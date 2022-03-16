# DP : 다시 사용 안하게 값을 기록하는 느낌으로 쭉쭉(누적)

import sys
N = int(sys.stdin.readline().rstrip())
house = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(N)]

for i in range(1, N):
    house[i][0] = min(house[i-1][1], house[i-1][2]) + house[i][0]
    house[i][1] = min(house[i-1][0], house[i-1][2]) + house[i][1]
    house[i][2] = min(house[i-1][0], house[i-1][1]) + house[i][2]

print(min(house[N-1]))