T = int(input())
want_to_sort = []

for _ in range(1, T+1):
    x, y = map(int, input().split())
    want_to_sort.append((x, y))

want_to_sort = sorted(want_to_sort, key= lambda x : (x[1], x[0]))

for i in want_to_sort:
    print(*i)


'''
from sys import stdin

input = stdin.readline
l = [input() for _ in range(int(input()))]
l.sort(key=lambda a: (int(a.split()[1]), int(a.split()[0])))
print("".join(l))
'''