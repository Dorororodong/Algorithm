N = int(input())
my_score = list(map(int, input().split()))
max_score = max(my_score)

for i in range(N):
    my_score[i] = (my_score[i] / max_score) * 100

print(sum(my_score)/N)

# list for문에 돌려서 바꿔주면 계속 바뀐다 조심혀라!