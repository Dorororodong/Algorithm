'''
이진수 덧셈은 매우 간단하고, 십진수 덧셈과 비슷하게 하면 된다.
십진수 덧셈을 할 때는, 오른쪽부터 왼쪽으로 차례대로 숫자 하나씩 더하면 된다.
이진수 덧셈도 이와 비슷하게 하면 된다. 십진수 덧셈은 외워야 할 덧셈이 많지만, 이진수 덧셈은 아래와 같이 5가지만 기억하면 된다.

0 + 0 = 0
1 + 0 = 1
0 + 1 = 1
1 + 1 = 10
1 + 1 + 1 = 11
두 이진수가 주어졌을 때, 그 합을 이진수로 출력하는 프로그램을 작성하시오.

첫째 줄에 테스트 케이스의 수 T(1<=T<=1,000)가 주어진다.
각 테스트 케이스는 숫자 2개로 이루어져있다. 이 숫자는 0과 1로만 이루어진 이진수이며, 길이는 최대 80자리이다.
(덧셈 결과는 81자리가 될 수도 있다) 이진수는 0으로 시작할 수도 있다.

각 테스트 케이스에 대해 입력으로 주어진 두 이진수의 합을 구해 이진수로 출력한다. 숫자의 앞에 불필요한 0이 붙으면 안 된다.
'''

import sys

T = int(sys.stdin.readline().rstrip())

for _ in range(1, T+1):
    a, b = sys.stdin.readline().rstrip().split()

    print(bin(int(a, 2) + int(b, 2))[2:])

'''
import sys

T = int(sys.stdin.readline().rstrip())

for _ in range(1, T+1):
    a, b = sys.stdin.readline().rstrip().split()

    result = int(a, 2) + int(b, 2)
    answer = ''

    if result == 0:
        print(0)

    else:
        while result != 0:
            answer += str(result % 2)
            result = result // 2

        print(answer[::-1])
'''