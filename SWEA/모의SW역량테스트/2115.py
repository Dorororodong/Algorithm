'''
N*N 개의 벌통
각 칸의 숫자는 각각의 벌통에 있는 꿀의 양을 나타내며, 꿀의 양은 서로 다를 수 있다.

두 명의 일꾼
채취할 수 있는 벌통의 수 M, 가로로 연속되도록 M개의 벌통을 선택
단, 두 명의 일꾼이 선택한 벌통은 서로 겹치면 안 된다.

두 일꾼이 채취할 수 있는 꿀의 최대 양은 C (2개 합해서 C초과이면, max로 넣어줌)

이익은 넣어준거 각각 제곱의 합
최대이익 출력!

(3 ≤ N ≤ 10)
(1 ≤ M ≤ 5)
M은 반드시 N 이하
(10 ≤ C ≤ 30)
하나의 벌통에서 채취할 수 있는 꿀의 양은 1 이상 9 이하의 정수
하나의 벌통에서 일부분의 꿀만 채취할 수 없고, 벌통에 있는 모든 꿀을 한번에 채취
'''


def find_honey(m, n):       # m : M 채취가로 / n : 0이면 처음, 1이면 그다음, 2일때 종료
    global max_profit

    # def find_max_comb(l, c):
    #     nonlocal profit
    #
    #     sorted(l)
    #     for u in l:
    #         if sum(l) - u <= c:
    #             for s in l:
    #                 if s != u:
    #                     profit += s ** 2
    #             return
    #         else:
    #             continue

    if n == 2:
        profit = 0
        for i in stack:
            if sum(i) > C:      # 여기를 어떻게 할까
                find_max_comb(i, C)

            else:
                for j in i:
                    profit += j ** 2

        if profit > max_profit:
            max_profit = profit
            return
        else:
            return

    for i in range(N):
        for j in range(N-m+1):      # N-m+1 = 3 / 0,1,2까지만 범위 설정(가능한)

            if visited[i][j] == 0:

                if visited[i][j+m-1] == 0:

                    for k in range(m):
                        visited[i][j+k] = 1
                        stack[n].append(honey[i][j + k])

                    find_honey(m, n+1)

                    for k in range(m):
                        visited[i][j+k] = 0
                        stack[n].pop()

                else:
                    break
            else:
                break

import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N, M, C = map(int, input().split())     # N : 전체가로 / M : 채취가로 / C :최대양

    honey = [list(map(int, input().split())) for _ in range(N)]
    # print(honey)
    visited = [[0] * N for _ in range(N)]
    max_profit = 0

    stack = [[], []]

    find_honey(M, 0)

    print('#{} {}'.format(tc, max_profit))

#1 174
#2 131
#3 145
#4 155
#5 166
#6 239
#7 166
#8 172
#9 291
#10 464