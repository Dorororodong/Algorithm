T = int(input())

for tc in range(1, T+1):
    word = list(input())

    collection = ['a', 'e', 'i', 'o', 'u']

    for i in collection:
        for _ in range(word.count(i)):
            word.remove(i)

    print('#{} {}'.format(tc, ''.join(word)))