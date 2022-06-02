import sys

temperature = []

while True:
    temp = float(sys.stdin.readline().rstrip())

    if temp == 999:
        break

    else:
        temperature.append(temp)

for i in range(1, len(temperature)):
    print('{:.2f}'.format(temperature[i] - temperature[i-1]))