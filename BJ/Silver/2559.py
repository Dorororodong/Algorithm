import sys
N, K = map(int, sys.stdin.readline().rstrip().split())
temp = list(map(int, sys.stdin.readline().rstrip().split()))
result = [sum(temp[:K])]

for i in range(N-K):
    result.append(result[i] + temp[i+K] - temp[i])

print(max(result))