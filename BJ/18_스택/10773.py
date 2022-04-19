T = int(input())
stack = []

for tc in range(1, T+1):
    N = int(input())
    if N > 0:
        stack.append(N)
    else:
        stack.pop()

print(sum(stack))


'''
from sys import stdin
input()
l=[]
for i in map(int, stdin):
    l.append(i) if i else l.pop()
print(sum(l))
'''