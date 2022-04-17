import sys
word = sys.stdin.readline().rstrip()
N = len(word)
cnt = 0

while N > 0:
    print(word[cnt:cnt + 10])
    cnt += 10
    N -= 10