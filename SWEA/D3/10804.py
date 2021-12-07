T = int(input())

for tc in range(1, T+1):
    word = list(input())[::-1]

    for i in range(len(word)):
        if word[i] == 'b':
            word[i] = 'd'
        elif word[i] == 'd':
            word[i] = 'b'
        elif word[i] == 'p':
            word[i] = 'q'
        else:
            word[i] = 'p'

    print('#{} {}'.format(tc, ''.join(word)))
