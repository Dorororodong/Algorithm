import sys
N = int(sys.stdin.readline())
result = [0] * 10001

for _ in range(N):
    result[int(sys.stdin.readline())] += 1

for i in range(1, 10001):
    if result[i] != 0:
        for j in range(result[i]):
            print(i)

'''
메모리 제한?!
일일이 append보다
10000번만 탐색하게 (최종적으로 10000번+10000번)
'''