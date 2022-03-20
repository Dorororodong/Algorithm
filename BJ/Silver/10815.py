def binary_search(list, find_number):
    start = 0
    end = len(list) - 1

    while start <= end:
        mid = (start + end) // 2

        if list[mid] == find_number:
            print(1, end=' ')
            return

        elif list[mid] < find_number:
            start = mid + 1

        else:
            end = mid - 1

    print(0, end=' ')

import sys
N = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().rstrip().split()))
A.sort()

M = int(sys.stdin.readline())
B = list(map(int, sys.stdin.readline().rstrip().split()))

for i in B:
    binary_search(A, i)