import sys
word1 = list(sys.stdin.readline().rstrip())
word2 = list(sys.stdin.readline().rstrip())

dp1 = [0] * 26
dp2 = [0] * 26

for i in word1:
    dp1[ord(i) - 97] += 1

for i in word2:
    dp2[ord(i) - 97] += 1

res = 0

for j in range(26):
    res += abs(dp1[j] - dp2[j])

print(res)