import sys
T = int(sys.stdin.readline().rstrip())

for _ in range(T):
    word = sys.stdin.readline().rstrip().split(' ')

    for i in range(len(word)):
        word[i] = word[i][::-1]

    print(' '.join(word))