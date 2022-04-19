from collections import deque
import sys
my_list = deque()
N = int(input())
for _ in range(N):
    num = sys.stdin.readline().split()
    if num[0] == 'push_front':
        my_list.appendleft(num[1])
    elif num[0] == 'push_back':
        my_list.append(num[1])
    elif num[0] == 'pop_front':
        if len(my_list) != 0:
            print(my_list.popleft())
        else:
            print(-1)
    elif num[0] == 'pop_back':
        if len(my_list) != 0:
            print(my_list.pop())
        else:
            print(-1)
    elif num[0] == 'size':
        print(len(my_list))
    elif num[0] == 'empty':
        if len(my_list) == 0:
            print(1)
        else:
            print(0)
    elif num[0] == 'front':
        if len(my_list) != 0:
            print(my_list[0])
        else:
            print(-1)
    else:
        if len(my_list) != 0:
            print(my_list[-1])
        else:
            print(-1)