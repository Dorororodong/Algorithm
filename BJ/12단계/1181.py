N = int(input())

word_list = []

for _ in range(N):
    word = input()

    if word not in word_list:
        word_list.append(word)

word_list.sort(key=len)

for i in range(len(word_list)-1):
    for j in range(i, len(word_list)):
        if len(word_list[i]) == len(word_list[j]) and word_list[i] > word_list[j]:
            word_list[i], word_list[j] = word_list[j], word_list[i]

for i in word_list:
    print(i)