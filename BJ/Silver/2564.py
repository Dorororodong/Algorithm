'''
첫째 줄에 블록의 가로의 길이와 세로의 길이가 차례로 주어진다.

둘째 줄에 상점의 개수가 주어진다.
블록의 가로의 길이와 세로의 길이, 상점의 개수는 모두 100이하의 자연수이다.

이어 한 줄에 하나씩 상점의 위치가 주어진다.
상점의 위치는 두 개의 자연수로 표시된다.

첫째 수는 상점이 위치한 방향을 나타내는데,
1은 블록의 북쪽, 2는 블록의 남쪽, 3은 블록의 서쪽, 4는 블록의 동쪽에 상점이 있음을 의미한다.

둘째 수는 상점이 블록의 북쪽 또는 남쪽에 위치한 경우 블록의 왼쪽 경계로부터의 거리를 나타내고,
상점이 블록의 동쪽 또는 서쪽에 위치한 경우 블록의 위쪽 경계로부터의 거리를 나타낸다.
마지막 줄에는 동근이의 위치가 상점의 위치와 같은 방식으로 주어진다. 상점의 위치나 동근이의 위치는 블록의 꼭짓점이 될 수 없다.

첫째 줄에 동근이의 위치와 각 상점 사이의 최단 거리의 합을 출력한다.
'''

import sys

W, H = map(int, sys.stdin.readline().rstrip().split())      # W 가로 / H 세로

T = int(sys.stdin.readline().rstrip())

stores = [tuple(map(int, sys.stdin.readline().rstrip().split())) for _ in range(T)]

dongkeun = tuple(map(int, sys.stdin.readline().rstrip().split()))

result = 0

for i in stores:
    if dongkeun[0] == 1:    # 북쪽
        if i[0] == 1:
            result += abs(dongkeun[1] - i[1])

        elif i[0] == 2:
            result += (H + min(dongkeun[1] + i[1], 2 * W - (dongkeun[1] + i[1])))

        elif i[0] == 3:
            result += (dongkeun[1] + i[1])

        else:
            result += (W - dongkeun[1] + i[1])

    elif dongkeun[0] == 2:  # 남쪽
        if i[0] == 1:
            result += (H + min(dongkeun[1] + i[1], 2 * W - (dongkeun[1] + i[1])))

        elif i[0] == 2:
            result += abs(dongkeun[1] - i[1])

        elif i[0] == 3:
            result += (dongkeun[1] + H - i[1])

        else:
            result += (W - dongkeun[1] + H - i[1])

    elif dongkeun[0] == 3:  # 서쪽
        if i[0] == 1:
            result += (dongkeun[1] + i[1])

        elif i[0] == 2:
            result += (H - dongkeun[1] + i[1])

        elif i[0] == 3:
            result += abs(dongkeun[1] - i[1])

        else:
            result += (W + min(dongkeun[1] + i[1], 2 * H - (dongkeun[1] + i[1])))

    else:                   # 동쪽
        if i[0] == 1:
            result += (W + dongkeun[1] - i[1])

        elif i[0] == 2:
            result += (W - dongkeun[1] + H - i[1])

        elif i[0] == 3:
            result += (W + min(dongkeun[1] + i[1], 2 * H - (dongkeun[1] + i[1])))

        else:
            result += abs(dongkeun[1] - i[1])

print(result)