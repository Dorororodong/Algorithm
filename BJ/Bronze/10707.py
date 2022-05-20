import sys
A = int(sys.stdin.readline().rstrip())
B = int(sys.stdin.readline().rstrip())
C = int(sys.stdin.readline().rstrip())
D = int(sys.stdin.readline().rstrip())
P = int(sys.stdin.readline().rstrip())

X_cost = A * P

Y_cost = 0

if C >= P:
    Y_cost = B

else:
    Y_cost = B + (P - C) * D

print(min(X_cost, Y_cost))