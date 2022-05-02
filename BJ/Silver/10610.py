import sys
N = sys.stdin.readline().rstrip()

mirco = list(N)
mirco.sort(reverse=True)

if mirco[-1] != '0':
    print(-1)

else:
    if sum(map(int, mirco)) % 3:
        print(-1)

    else:
        print(''.join(mirco))