import sys
sys.stdin = open('input.txt')

dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

T = int(input())
for tc in range(1, T+1):
    N, M, K = map(int, input().split())     # N : 세로 / M : 가로 / K : 시간

    cell = [list(map(int, input().split())) for _ in range(N)]
    # print(cell)

    vessel = [[0] * 351 for _ in range(351)]
    # print(vessel)



    # print('#{} {}'.format(tc, ))


#1 22
#2 36
#3 90
#4 164
#5 712