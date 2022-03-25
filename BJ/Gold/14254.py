# defaultdict, Counter 등을 사용하는 것을 두려워 하지마셈 [특히 문자열에서!]

def word_cnt(word_list):
    global cnt
    word_counter = Counter(word_list)
    cnt += len(word_list) - max(word_counter.values())

import sys
from collections import Counter
word = sys.stdin.readline().rstrip()
K = int(sys.stdin.readline().rstrip())
cnt = 0

if len(word) == K:
    print(cnt)

elif len(word) // 2 >= K:
    front = word[:K]
    back = word[-K:]

    for i in range(K):
        if front[i] != back[i]:
            cnt += 1

    print(cnt)

else:
    for i in range(len(word) - K):
        word_list = []
        for j in range(i, len(word), len(word) - K):
            word_list.append(word[j])

        word_cnt(word_list)

    print(cnt)