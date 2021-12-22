import sys

one = list(map(int, sys.stdin.readline().rstrip().split()))
two = list(map(int, sys.stdin.readline().rstrip().split()))

print(max(sum(one), sum(two)))