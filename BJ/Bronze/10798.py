import sys
max_length = 0
res = ''

board = [[-1] * 5 for _ in range(15)]

for j in range(5):
    word = sys.stdin.readline().rstrip()
    len_word = len(word)

    for i in range(len_word):
        board[i][j] = word[i]

    if max_length < len_word:
        max_length = len_word

for i in range(max_length):
    for j in board[i]:
        if j != -1:
            res += j

print(res)