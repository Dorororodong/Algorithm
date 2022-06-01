import sys
N = int(sys.stdin.readline().rstrip())
exam = list(map(int, sys.stdin.readline().rstrip().split()))

total = 0
exam_score = 0

for i in exam:
    if i == 1:
        exam_score += 1
        total += exam_score

    else:
        exam_score = 0

print(total)