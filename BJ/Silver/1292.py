import sys
A, B = map(int, sys.stdin.readline().rstrip().split())

math_problems = []

for i in range(1, 46):
    for _ in range(i):
        math_problems.append(i)

print(sum(math_problems[A-1:B]))