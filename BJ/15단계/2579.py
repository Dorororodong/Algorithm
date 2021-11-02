import sys
sys.stdin = open('input.txt')

N = int(input())
dp = []
for _ in range(N):
    dp.append(int(input()))

result = dp[-1]
dp_cnt = N - 1
duple_cnt = 0

while dp_cnt > 1:
    if dp[dp_cnt-1] >= dp[dp_cnt-2]:
        if duple_cnt == 0:              # 아직 중복 아니면 1칸가고
            result += dp[dp_cnt-1]
            dp_cnt -= 1
            duple_cnt += 1
        else:                           # 이미 붙어서 중복을 갔으면, 2칸을 가야된다
            result += dp[dp_cnt - 2]
            dp_cnt -= 2
            duple_cnt = 0
    else:
        result += dp[dp_cnt-2]
        dp_cnt -= 2
        duple_cnt = 0
                                        # 메모이제이션? / 썼던 걸 기록!
if dp_cnt == 0:
    print(result)
else:
    if duple_cnt == 0:
        print(result + dp[0])
    else:
        print(result)