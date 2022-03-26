# DP...
import sys
T = int(sys.stdin.readline().rstrip())

for _ in range(T):
    N, M = map(int, sys.stdin.readline().rstrip().split())
    dp = [[0] * (M + 1) for _ in range(N + 1)]
    for i in range(1, N+1):
        for j in range(1, M+1):
            if i == 1:                  # 출발이 1개라면, 무조건 도착 갯수
                dp[i][j] = j
                continue                # 바로 반복문으로 가시고

            if i == j:                  # 출발 = 도착, 무조건 1개
                dp[i][j] = 1

            else:
                if i < j:               # 여기가 실제로 DP 개념인데... / 위를 바탕으로 표를 그려보면 이해하기 쉬움
                    dp[i][j] = dp[i][j-1] + dp[i-1][j-1]

    print(dp[N][M])

'''
import sys, math
T = int(sys.stdin.readline().rstrip())

for _ in range(T):
    N, M = map(int, sys.stdin.readline().rstrip().split())
    print(math.factorial(M) // math.factorial(N) // math.factorial(M-N))
'''