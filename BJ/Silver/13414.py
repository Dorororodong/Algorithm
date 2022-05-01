import sys
K, L = map(int, sys.stdin.readline().rstrip().split())

application = {}

for i in range(L):
    student_num = sys.stdin.readline().rstrip()
    application[student_num] = i

application = sorted(application.items(), key=lambda x: x[1])

for i in application[:K]:
    print(i[0])