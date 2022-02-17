import sys
T = int(sys.stdin.readline().rstrip())
Yonsei = 0
Korea = 0

for _ in range(T):
    for _ in range(9):
        Y, K = map(int, sys.stdin.readline().rstrip().split())
        Yonsei += Y
        Korea += K

    if Yonsei > Korea:
        print('Yonsei')

    elif Yonsei < Korea:
        print('Korea')

    else:
        print('Draw')