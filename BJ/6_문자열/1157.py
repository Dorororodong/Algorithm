import sys
word = sys.stdin.readline().rstrip().upper()

set_word = set(word)
cnt_list = [0]
result = ''

for i in set_word:
    if max(cnt_list) > word.count(i):
        continue

    else:
    # elif max(cnt_list) <= word.count(i):
        cnt_list.append(word.count(i))
        result = i

if cnt_list.count(max(cnt_list)) < 2:
    print(result)
else:
    print('?')

'''
import sys
word = sys.stdin.readline().rstrip().upper()

word_set = set(word)
cnt = 0
result = ''

for i in word_set:
    if cnt == 0:
        cnt += word.count(i)
        result = i

    else:
        if cnt == word.count(i):
            result = '?'
            break

        elif cnt < word.count(i):
            cnt = word.count(i)
            result = i

print(result)
'''