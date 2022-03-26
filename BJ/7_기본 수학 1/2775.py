import sys

T = int(sys.stdin.readline().rstrip())

floor = [[i for i in range(1, 15)]]

for i in range(14):
    up_floor = []
    for j in range(14):
        up_floor.append(sum(floor[i][:j+1]))
    floor.append(up_floor)

for tc in range(1, T+1):
    k = int(sys.stdin.readline().rstrip())
    n = int(sys.stdin.readline().rstrip())

    print(floor[k][n-1])

'''
import sys
input = sys.stdin.readline

for _ in range(int(input())):
    k = int(input())
    n = int(input())

    people = [i for i in range(n + 1)]

    for i in range(k):
        for j in range(1, n + 1):
            people[j] = people[j] + people[j - 1]

    print(people[-1])
    
    # 답만 필요하니까 생성 X / 쌓아나가면 된다!...
'''