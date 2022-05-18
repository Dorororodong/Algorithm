import sys
num_8 = sys.stdin.readline().rstrip()

num = int(num_8, 8)

print(bin(num)[2:])