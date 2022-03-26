import sys

T = int(input())
stack = []

for tc in range(1, T+1):
    command = sys.stdin.readline().split()       # 알아서 나누고 리스트에 넣어줌

    if command[0] == 'push':
        stack.append(command[1])

    elif command[0] == 'pop':
        if len(stack) > 0:
            print(stack.pop())

        else:
            print(-1)

    elif command[0] == 'size':
        print(len(stack))

    elif command[0] == 'empty':
        if len(stack) == 0:
            print(1)

        else:
            print(0)

    else:   # top
        if len(stack) > 0:
            print(stack[-1])

        else:
            print(-1)