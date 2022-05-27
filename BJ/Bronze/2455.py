import sys
passenger = [0]

for i in range(4):
    get_off, get_in = map(int, sys.stdin.readline().rstrip().split())

    passenger.append(passenger[i] + get_in - get_off)

print(max(passenger))