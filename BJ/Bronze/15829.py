import sys

L = int(sys.stdin.readline().rstrip())
word = sys.stdin.readline().rstrip()
result = 0

for i in range(L):
    result += (ord(word[i])-96) * (31 ** i)

print(result % 1234567891)