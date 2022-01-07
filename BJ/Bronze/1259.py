import sys

while True:
    word = sys.stdin.readline().rstrip()
    if word == '0':
        break
    else:
        if word == word[::-1]:
            print('yes')
        else:
            print('no')

# 펠린드롬은 좌우 반전... ㅅㅂ...
# 너무 어렵게 생각 ㄴㄴ... 헛수고만 했네... 아....