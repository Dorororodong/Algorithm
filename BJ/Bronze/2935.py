import sys
A = int(sys.stdin.readline().rstrip())
oper = sys.stdin.readline().rstrip()
B = int(sys.stdin.readline().rstrip())

if oper == '*':
    print(A * B)
else:
    print(A + B)