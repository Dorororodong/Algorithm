'''
0001100
'''

import sys
sys.stdin = open('input.txt')

word = input()

cnt_0 = 0
cnt_1 = 0
pre_num = word[0]

for i in range(1, len(word)):

    if word[i] == '0' and word[i] != pre_num:
        cnt_1 += 1
        pre_num = '0'

    elif word[i] == '1' and word[i] != pre_num:
        cnt_0 += 1
        pre_num = '1'

if pre_num == '0':
    cnt_0 += 1

else:
    cnt_1 += 1

print(min(cnt_0, cnt_1))

# 1