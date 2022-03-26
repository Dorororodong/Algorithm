'''
올림  ceil
내림  floor, trunc(like int)
반올림 round
'''

import sys
import math

A, B, V = map(int, sys.stdin.readline().rstrip().split())
print(1 + math.ceil((V-A) / (A-B)))