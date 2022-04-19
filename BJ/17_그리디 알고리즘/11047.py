N, K = map(int, input().split())

money_list = []
cnt = 0

for tc in range(1, N+1):
    money_list.append(int(input()))

for i in range(N-1, -1, -1):
    if money_list[i] <= K:
        cnt += K // money_list[i]
        K = K % money_list[i]

    if K == 0:
        break

print(cnt)


'''
N, K = map(int, input().split())

Coins = []
for i in range(N) : Coins.append(int(input()))


ans = 0
while K > 0 :
    coin = Coins.pop()
    ans += K // coin
    K %= coin

print(ans)
'''