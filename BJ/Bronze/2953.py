import sys
participant = []
winner = 0

for _ in range(5):
    score = sum(map(int, sys.stdin.readline().rstrip().split()))
    participant.append(score)

    if winner < score:
        winner = score

print(participant.index(winner) + 1, winner)