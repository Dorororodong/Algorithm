import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    fee = list(map(int, input().split()))       # 1일, 1달 (같이 움직) / 3달 / 1년(마지막에 1번만 사용)
    plan = list(map(int, input().split()))
    # print(fee)
    # print(plan)

    dp = [0] * 13       # 1~12월, 0월은 1월부터 계산들어가면 있어야함 (전달 더하기니까)

    for i in range(12):     # 달력 돌면서
        if plan[i] == 0:
            dp[i+1] = dp[i]     # 0이면 비용이 그대로 진행
        else:
            if i < 2:           # 1, 2월까지는 3달비용 의미 없음
                dp[i+1] = dp[i] + min(plan[i] * fee[0], fee[1])     # 이전꺼 더하기 / 1일이랑 1달중에 최소비용

            else:
                dp[i+1] = min(dp[i] + plan[i] * fee[0], dp[i] + fee[1], dp[i-2] + fee[2])       # 1일, 1달, 3달 중 최소비용 (3달은 3달전꺼 더하기)

    print('#{} {}'.format(tc, min(dp[-1], fee[-1])))        # 마지막 1년은 최종 비용이랑 비교

'''
#1 110
#2 100
#3 400
#4 530
#5 430
#6 1080
#7 1840
#8 800
#9 1980
#10 2260
'''