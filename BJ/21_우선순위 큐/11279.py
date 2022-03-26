# 최대힙!
import heapq
import sys

N = int(sys.stdin.readline().rstrip())

heap = []

for _ in range(N):
    x = int(sys.stdin.readline().rstrip())

    if x == 0:
        if len(heap) == 0:
            print(0)

        else:
            print(heapq.heappop(heap)[1])

    else:
        heapq.heappush(heap, (-x, x))


'''
from sys import stdin
input = stdin.readline

from heapq import heappop, heappush, heapify

heap = []
heapify(heap)

N = int(input())

for _ in range(N):
  x = int(input())

  if x == 0:
    if heap:
      print(-1 * heappop(heap))
    else:
      print(0)
  else:
    heappush(heap, -1 * x)
'''