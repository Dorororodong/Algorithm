def binary_search_count(data, find):
    start = 0
    end = len(data) - 1

    while start <= end:
        mid = (start + end) // 2

        if data[mid] == find:
            print(have.count(find), end=' ')
            return

        elif data[mid] > find:
            end = mid - 1

        else:
            start = mid + 1

    print(0, end=' ')

import sys
N = int(sys.stdin.readline().rstrip())
have = sorted(list(map(int, sys.stdin.readline().rstrip().split())))

M = int(sys.stdin.readline().rstrip())
find = list(map(int, sys.stdin.readline().rstrip().split()))

for i in find:
    binary_search_count(have, i)