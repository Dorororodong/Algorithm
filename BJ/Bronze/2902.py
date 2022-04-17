import sys
word = sys.stdin.readline().rstrip().split('-')
ans = ''

for i in word:
    ans += i[0]

print(ans)