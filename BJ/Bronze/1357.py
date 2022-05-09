def rev(w):
    res = ''
    flag = True

    for i in range(len(w) - 1, -1, -1):
        if w[i] != '0':
            flag = False
            res += w[i]

        else:
            if flag == False:
                res += w[i]

    return res

import sys
x, y = sys.stdin.readline().rstrip().split()

print(rev(str(int(rev(x)) + int(rev(y)))))

'''
import sys
x, y = sys.stdin.readline().rstrip().split()

print(int(str(int(x[::-1]) + int(y[::-1]))[::-1]))
'''