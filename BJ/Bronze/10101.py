import sys
r1 = int(sys.stdin.readline().rstrip())
r2 = int(sys.stdin.readline().rstrip())
r3 = int(sys.stdin.readline().rstrip())

if r1 == r2 == r3 == 60:
    print('Equilateral')

elif r1 + r2 + r3 == 180 and (r1 == r2 or r2 == r3 or r3 == r1):
    print('Isosceles')

elif r1 + r2 + r3 == 180 and r1 != r2 != r3:
    print('Scalene')

else:
    print('Error')