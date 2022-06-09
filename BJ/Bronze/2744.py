import sys
word = sys.stdin.readline().rstrip()

word_rev = ''

for i in word:
    if i.islower():
        word_rev += i.upper()

    else:
        word_rev += i.lower()

print(word_rev)