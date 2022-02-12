import sys

N = int(sys.stdin.readline().rstrip())
Participant = list(map(int, sys.stdin.readline().rstrip().split()))
Wait = [0] * N

cnt = 0
while Participant.count(0) != N:
    for i in range(N):
        if Participant[i] != 0:
            cnt += 1
            Participant[i] -= 1
            Wait[i] = cnt

print(*Wait)