import sys
grade = sys.stdin.readline().rstrip()

if grade[0] == 'F':
    print(0.0)

else:
    if grade[1] == '+':
        print(69 - ord(grade[0]) + 0.3)
    elif grade[1] == '-':
        print(69 - ord(grade[0]) - 0.3)
    else:
        print('{:.1f}'.format(69 - ord(grade[0])))