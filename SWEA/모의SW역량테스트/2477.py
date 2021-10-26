'''
고객만족도 설문지에는 고객이 이용했던 접수 창구번호와 정비 창구번호가 있다.
차량 정비소에는 N개의 접수 창구와 M개의 정비 창구가 있다.
접수 창구는 1부터 N까지 번호가 붙어 있다. 정비 창구도 1부터 M까지 번호가 붙어 있다.
첫 단계는 접수 창구에서 고장을 접수하는 것이고, 두 번째 단계는 정비 창구에서 차량을 정비하는 것이다.

한 담당자의 처리 시간은 고객과 고장의 종류에 상관 없이 항상 같다.
접수 창구 i에서 고객 한 명의 고장을 접수하는 데 걸리는 처리 시간은 ai이다. (1 ≤ i ≤ N)
정비 창구 j에서 고객 한 명의 차량을 정비하는 데 걸리는 처리 시간은 bj이다. (1 ≤ j ≤ M)

지금까지 차량 정비소를 방문한 고객은 K명이다.
고객은 도착하는 대로 1번부터 고객번호를 부여 받는다.
고객번호 k의 고객이 차량 정비소에 도착하는 시간은 tk이다. (1 ≤ k ≤ K)

고객이 차량 정비소에 도착하면, 빈 접수 창구가 있는 경우 빈 접수 창구에 가서 고장을 접수한다.
빈 접수 창구가 없는 경우 빈 접수 창구가 생길 때까지 기다린다.
고장 접수를 완료하면 정비 창구로 이동한다.
빈 정비 창구가 있는 경우 빈 정비 창구에 가서 차량을 정비 받는다.
빈 정비 창구가 없는 경우 빈 정비 창구가 생길 때까지 기다린다.

접수 창구의 우선순위는 아래와 같다.
① 여러 고객이 기다리고 있는 경우 고객번호가 낮은 순서대로 우선 접수한다.
② 빈 창구가 여러 곳인 경우 접수 창구번호가 작은 곳으로 간다.

정비 창구의 우선순위는 아래와 같다.
① 먼저 기다리는 고객이 우선한다.
② 두 명 이상의 고객들이 접수 창구에서 동시에 접수를 완료하고 정비 창구로 이동한 경우, 이용했던 접수 창구번호가 작은 고객이 우선한다.
③ 빈 창구가 여러 곳인 경우 정비 창구번호가 작은 곳으로 간다.

고객이 차량 정비소에 도착하여 접수 창구로 가는 시간 또는 접수 창구에서 정비 창구로 이동하는 시간은 무시할 수 있다. 즉, 이동 시간은 0이다.
고객의 도착 시간 tk, 접수 창구의 처리 시간 ai, 정비 창구의 처리 시간 bj가 주어졌을 때,
지갑을 분실한 고객과 같은 접수 창구와 같은 정비 창구를 이용한 고객의 고객번호들을 찾아 그 합을 출력하는 프로그램을 작성하라.
만약, 그런 고객이 없는 경우 -1을 출력한다.

(1 ≤ N, M ≤ 9)
(1 ≤ ai ≤ 20)
(1 ≤ bj ≤ 20)
(2 ≤ K ≤ 1,000)
(0 ≤ tk ≤ 1,000)
(1 ≤ A ≤ N)
(1 ≤ B ≤ M)
창구번호와 고객번호는 1부터 시작한다.

'''

import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N, M, K, A, B = map(int, input().split())       # N(접수창구 갯수) / M(정비창구 갯수) / K(고객 수) / 접수번호(A) / 정비번호(B)
    ai = list(map(int, input().split()))            # 접수창구 시간들
    bj = list(map(int, input().split()))            # 정비창구 시간들
    tk = list(map(int, input().split()))            # 손님방문 시간들
    # print(ai)
    # print(bj)
    # print(tk)



#1 3
#2 7
#3 2
#4 22
#5 18
#6 15
#7 -1
#8 259
#9 100
#10 164