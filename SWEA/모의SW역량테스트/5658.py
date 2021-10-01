'''
각 변에 다음과 같이 16진수 숫자(0~F)가 적혀 있는 보물상자
보물 상자의 뚜껑은 시계방향으로 돌릴 수 있고, 한 번 돌릴 때마다 숫자가 시계방향으로 한 칸씩 회전

각 변에는 동일한 개수의 숫자가 있고, 시계방향 순으로 높은 자리 숫자에 해당하며 하나의 수를 나타낸다.

비밀번호는 보물 상자에 적힌 숫자로 만들 수 있는 모든 수 중, K번째로 큰 수를 10진 수로 만든 수이다.
N개의 숫자가 입력으로 주어졌을 때, 보물상자의 비밀 번호를 출력하는 프로그램을 만들어보자.
(서로 다른 회전 횟수에서 동일한 수가 중복으로 생성될 수 있다. 크기 순서를 셀 때 같은 수를 중복으로 세지 않도록 주의한다.)

N은 4의 배수이고, 8이상 28이하의 정수이다. (8 ≤ N ≤ 28)
N개의 숫자는 각각 0이상 F이하로 주어진다. (A~F는 알파벳 대문자로만 주어진다.)
K는 생성 가능한 수의 개수보다 크게 주어지지 않는다.

16진수 0~F 숫자가 공백 없이 N개 주어진다.
'''


from collections import deque       # pop은 했는데, 왼쪽에 어떻게 넣어주냐 이것말곤 없다
import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N, K = map(int, input().split())
    all_hex_list = []
    hex = list(input())     # 16진수 전체를 받고
    d_hex = deque(hex)      # 덱 사용

    for _ in range(N//4):
        original_hex = ''
        d_hex.appendleft(d_hex.pop())       # 오른쪽을 뽑아서 왼쪽에 넣는다
        # print(d_hex)
        for i in d_hex:
            original_hex += i               # 원래 글자형태로 다시 복구

        for i in range(N//4, N+1, N//4):        # 4면이니까, N//4씩 잘라줌
            if original_hex[(i - N//4) : i] not in all_hex_list:        # 중복은 넣어주지 말랬으니까
                all_hex_list.append(original_hex[(i - N//4) : i])       # 중복 빼고 리스트에 넣어줌!

    for i in range(len(all_hex_list)):
        all_hex_list[i] = int(all_hex_list[i], 16)      # 16진수를 10진수로!

    all_hex_list.sort(reverse=True)     # 내림차순

    print('#{} {}'.format(tc, all_hex_list[K-1]))       # K번째니까 K-1


#1 503
#2 55541
#3 334454
#4 5667473
#5 182189737