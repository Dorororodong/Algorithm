
def find_honey_and_make_profit(n, m):




import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N, M, C = map(int, input().split())     # N : 전체가로 / M : 채취가로 / C :최대양

    honey = [list(map(int, input().split())) for _ in range(N)]
    visited = [[0] * N for _ in range(N)]

    find_honey_and_make_profit(N, M)