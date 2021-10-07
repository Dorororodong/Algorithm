'''
우선 순위는 고려하지 않고 왼쪽에서 오른쪽으로 차례대로 계산
게임 판에 적힌 숫자의 개수 N( 3 ≤ N ≤ 12 )
연산자 카드 개수의 총 합은 항상 N - 1
게임 판에 적힌 숫자는 1 이상 9 이하의 정수
수식을 완성할 때 각 연산자 카드를 모두 사용해야
숫자와 숫자 사이에는 연산자가 1 개만 들어가야
나눗셈을 계산 할 때 소수점 이하는 버린다.
입력으로 주어지는 숫자의 순서는 변경할 수 없다.
정답은 만들 수 있는 수식으로 얻은 결과값 중 최댓값과 최솟값의 차이
'''

import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    operator_num = list(map(int, input().split()))      # + - * /
    number_list = list(map(int, input().split()))       # 순서보장
    result_list = []



    print('#{} {}'.format(tc, max(result_list) - min(result_list)))

#1 24
#2 8
#3 144
#4 8
#5 91
#6 150
#7 198
#8 2160
#9 46652
#10 701696