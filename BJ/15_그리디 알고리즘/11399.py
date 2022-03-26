N = int(input())
min_result = 0
bank = sorted(list(map(int, input().split())))

for i in range(N):
    min_result += bank[i] * (N-i)

print(min_result)