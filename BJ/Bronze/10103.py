import sys
n = int(sys.stdin.readline().rstrip())
young = 100
duck = 100

for _ in range(n):
    x, y = map(int, sys.stdin.readline().rstrip().split())

    if x > y:
        duck -= x

    elif x < y:
        young -= y

print(young)
print(duck)