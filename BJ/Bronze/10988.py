import sys
word = sys.stdin.readline().rstrip()

if word == word[::-1]:
    print(1)

else:
    print(0)