import sys
vowel = 'aeiouAEIOU'

while True:
    sentence = sys.stdin.readline().rstrip()

    vowel_cnt = 0

    if sentence == '#':
        break

    for i in sentence:
        if i in vowel:
            vowel_cnt += 1

    print(vowel_cnt)