T = int(input())

for tc in range(1, T+1):
    quiz = input()

    cnt = -1
    res = 0
    for i in range(len(quiz)):
        if quiz[i] == 'O':
            res += 1
            cnt += 1
            res = res + cnt

        else:
            cnt = -1

    print(res)


'''
import sys
N = int(sys.stdin.readline())
for i in range(N):
    quiz_result = sys.stdin.readline()
    accum = 1
    score = 0
    for q in quiz_result:
        if q is 'O':
            score += accum
            accum += 1
        else:
            accum = 1
    print(score)
'''
