import sys
word = sys.stdin.readline().rstrip().upper()

word_list = list(word)
cnt = 0
result = ''

for i in range(len(word_list)):
    if result == word_list[i]:
        continue
    if cnt == word_list.count(word_list[i]):
        result = '?'
        break
    elif cnt < word_list.count(word_list[i]):
        cnt = word_list.count(word_list[i])
        result = word_list[i]
print(result)



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