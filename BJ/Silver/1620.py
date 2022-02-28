import sys
N, M = map(int, sys.stdin.readline().rstrip().split())

pokemon = {}
cnt = 1

for _ in range(N):
    pokemon[sys.stdin.readline().rstrip()] = cnt
    cnt += 1

# 내장함수 reversed
reverse_pokemon = dict(map(reversed, pokemon.items()))

for _ in range(M):
    word = sys.stdin.readline().rstrip()

    if word.isdigit():
        print(reverse_pokemon[int(word)])

    else:
        print(pokemon[word])