import sys
N = int(sys.stdin.readline().rstrip())

changes = 1000 - N

cnt = 0

while changes != 0:
    if changes >= 500:
        cnt += changes // 500
        changes %= 500

    elif changes >= 100:
        cnt += changes // 100
        changes %= 100

    elif changes >= 50:
        cnt += changes // 50
        changes %= 50

    elif changes >= 10:
        cnt += changes // 10
        changes %= 10

    elif changes >= 5:
        cnt += changes // 5
        changes %= 5

    else:
        cnt += changes // 1
        changes %= 1

print(cnt)