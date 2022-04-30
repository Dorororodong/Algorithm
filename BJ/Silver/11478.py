import sys
S = sys.stdin.readline().rstrip()

N = len(S)
ans = set()

for i in range(N):
    for j in range(N-i):
        ans.add(S[j:j+i+1])

print(len(ans))