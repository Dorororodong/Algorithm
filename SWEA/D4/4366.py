
import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    # binary_to_decimal = int(input(), 2)
    # ternary_to_decimal = int(input(), 3)
    binary = list(map(int, input()))
    ternary = list(map(int, input()))
    # print(binary)
    # print(ternary)
    # print(binary_to_decimal)
    # print(ternary_to_decimal)
    # binary_list = []
    # for i in range(len(binary)):
    




    print('#{} {} {}'.format(tc, binary, ternary))