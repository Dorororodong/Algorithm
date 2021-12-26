'''
N (1 ≤ N ≤ 100)
색종이가 놓이는 평면은 가로 최대 1001칸, 세로 최대 1001칸으로 구성된 격자 모양이다.
격자의 각 칸은 가로, 세로 길이가 1인 면적이 1인 정사각형이다.

색종이가 놓인 상태는 가장 왼쪽 아래 칸의 번호와 너비, 높이를 나타내는 네 정수로 표현한다.
예를 들어, 위 그림에서 회색으로 표시된 색종이는 (1,4)가 가장 왼쪽 아래에 있고 너비 3, 높이 2이므로 1 4 3 2로 표현한다.
색종이가 격자 경계 밖으로 나가는 경우는 없다.

입력에서 주어진 순서에 따라 N장의 색종이를 평면에 놓았을 때,
입력에서 주어진 순서대로 각 색종이가 보이는 부분의 면적을 한 줄에 하나씩 하나의 정수로 출력한다.
만약 색종이가 보이지 않는다면 정수 0을 출력한다.
'''

import sys
N = int(sys.stdin.readline().rstrip())
if N == 1:
    x, y, a, b = map(int, sys.stdin.readline().rstrip().split())
    print(a * b)

else:
    arr = [[0] * 1001 for _ in range(1001)]
    cnt_list = [0] * (N + 1)

    for i in range(1, N+1):
        x, y, a, b = map(int, sys.stdin.readline().rstrip().split())

        for j in range(x, x+a):
            for k in range(y, y+b):
                arr[j][k] = i


    for k in range(1000, -1, -1):
        for l in range(1000, -1, -1):
            if arr[k][l] != 0:
                cnt_list[arr[k][l]] += 1

    for m in cnt_list[1:]:
        print(m)