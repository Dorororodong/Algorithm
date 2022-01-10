'''
2
3 3
3 1 2
4 1 4
2 2 2
2 4
7 3 1 8
3 3 3 4
'''

import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())

    cards = [min(map(int, input().split())) for _ in range(N)]

    print(max(cards))