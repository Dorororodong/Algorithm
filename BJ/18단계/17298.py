import sys

N = int(sys.stdin.readline().rstrip())
A = list(map(int, sys.stdin.readline().rstrip().split()))

for i in range(N-1):

    for j in range(i+1, N):
        if A[i] < A[j]:
            print(A[j], end=' ')
            break

        else:
            if j == N-1:
                print(-1, end=' ')
print(-1)

'''
import sys

N = int(sys.stdin.readline().rstrip())
A = list(map(int, sys.stdin.readline().rstrip().split()))

stack = []

for i in range(N-1):
    stack.append(-1)
    for j in A[i+1:]:
        if A[i] < j:
            stack.pop()
            stack.append(j)
            break
stack.append(-1)

print(*stack)
'''