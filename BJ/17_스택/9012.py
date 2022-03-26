import sys
T = int(sys.stdin.readline().rstrip())

for _ in range(T):
    stack = []
    flag = True
    parenthesis = sys.stdin.readline().rstrip()

    for i in parenthesis:
        if len(stack) == 0:
            if i == '(':
                stack.append(i)

            else:
                print('NO')
                flag = False
                break

        else:
            if i == '(':
                if stack[-1] == ')':
                    print('NO')
                    flag = False
                    break

                else:
                    stack.append(i)

            else:
                if stack[-1] == ')':
                    print('NO')
                    flag = False
                    break

                else:
                    stack.pop()

    if flag == True:
        if len(stack) == 0:
            print('YES')

        else:
            print('NO')


'''
# () 이거 한쌍이 제거 되야 되므로 계속 해서 없애주면서 최종 결과를 본다

from sys import stdin
input = stdin.readline
    
def VPS(li: str):
    while '()' in li:
        li = li.replace("()", "")
    if len(li) == 0: return "YES"
    else: return "NO" 

result =[]
iter = int(input())
for i in range(iter):
    array = input().strip()
    result.append(VPS(array))
print("\n".join(map(str, result)))
'''