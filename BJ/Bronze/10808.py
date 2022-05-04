import sys
word = sys.stdin.readline().rstrip()

alphabet = [0] * 26

for i in word:
    alphabet[ord(i) - 97] += 1

print(' '.join(map(str, alphabet)))