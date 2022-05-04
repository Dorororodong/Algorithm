import sys
from collections import Counter
N = int(sys.stdin.readline().rstrip())

for _ in range(N):
    a, b = sys.stdin.readline().rstrip().split()

    if Counter(a) == Counter(b):
        print('Possible')

    else:
        print('Impossible')

'''
import sys
N = int(sys.stdin.readline().rstrip())

for _ in range(N):
    a, b = sys.stdin.readline().rstrip().split()

    if sorted(list(a)) == sorted(list(b)):
        print('Possible')

    else:
        print('Impossible')
'''