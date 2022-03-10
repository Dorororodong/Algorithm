import sys
while True:
    word = sys.stdin.readline().rstrip()
    if word == '.':
        break

    stack = []

    for i in range(len(word)):
        if len(stack) == 0:
            if word[i] == '(' or word[i] == '[':
                stack.append(word[i])

            elif word[i] == ')' or word[i] == ']':
                print('no')
                break

        else:
            if word[i] == '(' or word[i] == '[':
                stack.append(word[i])

            if stack[-1] == '(':
                if word[i] == ')':
                    stack.pop()

                elif word[i] == ']':
                    print('no')
                    break

            elif stack[-1] == '[':
                if word[i] == ']':
                    stack.pop()

                elif word[i] == ')':
                    print('no')
                    break

    if i == len(word) - 1:
        if len(stack) == 0:
            print('yes')

        else:
            print('no')