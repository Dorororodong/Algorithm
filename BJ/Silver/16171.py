import sys

textbook = list(sys.stdin.readline().rstrip())
only_text_in_textbook = ''
find_please = sys.stdin.readline().rstrip()

for i in textbook:
    if i.isalpha():
        only_text_in_textbook += i

if find_please in only_text_in_textbook:
    print(1)

else:
    print(0)
