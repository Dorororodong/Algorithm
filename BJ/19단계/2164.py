from collections import deque

N = int(input())

card = deque([i for i in range(1, N+1)])

while len(card) > 1:
    card.popleft()
    card.append(card.popleft())

print(card[0])


'''
from collections import deque

N = int(input())

card = deque([i for i in range(1, N+1)])

while len(card) > 2:
    card.popleft()
    card.append(card.popleft())

print(card[-1])
'''