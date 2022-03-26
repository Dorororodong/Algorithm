# Brute Force: 조합 가능한 모든 경우를 하나씩 대입해 보는 방법
# Greedy: 현재 상황에서 지금 당장 좋은 것만 고르는 방법
# Dynamic Programming: 큰 문제를 한 번에 해결하기 힘들 때, 작은 여러 개의 문제로 나누어서 푸는 방법 [문제들을 반복해서 푸는 경우에 그 문제들을 매번 재계산하지 않고 값을 저장해두었다가 재사용]

# 이것은 그리디!
import sys
N = int(sys.stdin.readline().rstrip())

schedule = [tuple(map(int, sys.stdin.readline().rstrip().split())) for _ in range(N)]

schedule.sort(key=lambda x: (x[1], x[0]))

cnt = 1
end = schedule[0][1]

for i in range(1, len(schedule)):
    if end <= schedule[i][0]:
        cnt += 1
        end = schedule[i][1]

print(cnt)