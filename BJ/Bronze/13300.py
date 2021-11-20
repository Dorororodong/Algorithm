'''
정보 초등학교에서는 단체로 2박 3일 수학여행을 가기로 했다.
여러 학년이 같은 장소로 수학여행을 가려고 하는데 1학년부터 6학년까지 학생들이 묵을 방을 배정해야 한다.
남학생은 남학생끼리, 여학생은 여학생끼리 방을 배정해야 한다.
또한 한 방에는 같은 학년의 학생들을 배정해야 한다.
물론 한 방에 한 명만 배정하는 것도 가능하다.

한 방에 배정할 수 있는 최대 인원 수 K가 주어졌을 때,
조건에 맞게 모든 학생을 배정하기 위해 필요한 방의 최소 개수를 구하는 프로그램을 작성하시오.
'''

import sys

boys = []
girls = []
cnt = 0

N, K = map(int, sys.stdin.readline().split())       # 인원, 최대

for _ in range(N):
    S, Y = map(int, sys.stdin.readline().split())   # 성별, 학년

    if S == 0:
        girls.append(Y)
    else:
        boys.append(Y)

for i in range(1, 7):
    if 0 < boys.count(i) <= K:
        cnt += 1
    else:
        if boys.count(i) % K:
            cnt += (boys.count(i) // K + 1)
        else:
            cnt += (boys.count(i) // K)

    if 0 < girls.count(i) <= K:
        cnt += 1
    else:
        if girls.count(i) % K:
            cnt += (girls.count(i) // K + 1)
        else:
            cnt += (girls.count(i) // K)

print(cnt)