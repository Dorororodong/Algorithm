import sys
from itertools import combinations
N = int(sys.stdin.readline().rstrip())
soccers = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(N)]
nums = {i for i in range(N)}
comb = set(combinations(nums, N // 2))
result = 987654321

for i in comb:
    comb_opp = nums - set(i)
    syn1 = 0
    syn2 = 0
    comb1 = list(combinations(i, 2))
    comb2 = list(combinations(comb_opp, 2))

    for j in range(len(comb1)):
        syn1 += soccers[comb1[j][0]][comb1[j][1]] + soccers[comb1[j][1]][comb1[j][0]]
        syn2 += soccers[comb2[j][0]][comb2[j][1]] + soccers[comb2[j][1]][comb2[j][0]]

    if result > abs(syn1 - syn2):
        result = abs(syn1 - syn2)

print(result)