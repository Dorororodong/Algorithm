def binary_search(list, find_number):
    start = 0
    end = len(list) - 1

    while start <= end:
        mid = (start + end) // 2

        if list[mid] == find_number:
            print(1)
            return

        elif list[mid] < find_number:
            start = mid + 1

        else:
            end = mid - 1

    print(0)

import sys
N = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().rstrip().split()))
A.sort()

M = int(sys.stdin.readline())
B = list(map(int, sys.stdin.readline().rstrip().split()))

for i in B:
    binary_search(A, i)

'''
def binary_search_recursion(target, start, end, data):
    if start > end:
        return None

    mid = (start + end) // 2

    if data[mid] == target:
        return mid
    elif data[mid] > target:
        end = mid - 1
    else:
        start = mid + 1        

    return binary_search_recursion(target, start, end, data)
'''