'''
4 별 / 3 동 / 2 네 / 1 세
'''
import sys
N = int(sys.stdin.readline().rstrip())

for _ in range(N):
    A_list = list(map(int, sys.stdin.readline().rstrip().split()))
    B_list = list(map(int, sys.stdin.readline().rstrip().split()))
    cnt_a = A_list[0]
    cnt_b = B_list[0]
    A_list = A_list[1:]
    B_list = B_list[1:]

    if A_list.count(4) != B_list.count(4):
        if A_list.count(4) > B_list.count(4):
            print('A')

        else:
            print('B')

    elif A_list.count(3) != B_list.count(3):
        if A_list.count(3) > B_list.count(3):
            print('A')

        else:
            print('B')

    elif A_list.count(2) != B_list.count(2):
        if A_list.count(2) > B_list.count(2):
            print('A')

        else:
            print('B')

    elif A_list.count(1) != B_list.count(1):
        if A_list.count(1) > B_list.count(1):
            print('A')

        else:
            print('B')

    else:
        print('D')