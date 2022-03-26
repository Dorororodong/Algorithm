import sys
N = int(sys.stdin.readline().rstrip())
road = list(map(int, sys.stdin.readline().rstrip().split()))
gas = list(map(int, sys.stdin.readline().rstrip().split()))

ans = road[0] * gas[0]
min_gas = gas[0]

for i in range(1, N-1):
    if min_gas > gas[i]:
        min_gas = gas[i]

    ans += min_gas * road[i]

print(ans)