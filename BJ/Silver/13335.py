import sys
from collections import deque
n, w, L = map(int, sys.stdin.readline().rstrip().split())   # n : 트럭 수 / w : 다리 길이 / L : 다리 최대하중
trucks = deque(list(map(int, sys.stdin.readline().rstrip().split())))

bridge = deque([0] * w)
time = 0

while n:
    time += 1

    if trucks:
        if L >= trucks[0]:
            L -= trucks[0]
            bridge.append(trucks.popleft())

            if bridge[0] > 0:
                n -= 1
                L += bridge[0]
            bridge.popleft()

        else:
            if bridge[0] > 0:
                n -= 1
                L += bridge[0]
            bridge.popleft()

            if L >= trucks[0]:
                L -= trucks[0]
                bridge.append(trucks.popleft())

            else:
                bridge.append(0)

    else:
        if bridge[0] > 0:
            n -= 1
            L += bridge[0]
            bridge.popleft()
            bridge.append(0)

        else:
            bridge.append(bridge.popleft())

print(time)

'''
# 트럭대수, 다리길이, 최대하중
N, W, L = map(int, input().split())
# 각 트럭의 무게
trucks = list(map(int, input().split()))

bridge = [0] * W
bridge_sum = 0
time = 0
while trucks or bridge_sum:                     # or !
    time += 1
    bridge_sum -= bridge.pop(0)                 # 0을 빼든 무게를 빼든 어쨋든 상관 X
    if trucks and bridge_sum + trucks[0] <= L:  # and !
        bridge.append(trucks.pop(0))
        bridge_sum += bridge[-1]
    else:
        bridge.append(0)
print(time)
'''