import sys
L = int(sys.stdin.readline().rstrip())
A = int(sys.stdin.readline().rstrip())
B = int(sys.stdin.readline().rstrip())
C = int(sys.stdin.readline().rstrip())
D = int(sys.stdin.readline().rstrip())

no_play_day_kor = 0
no_play_day_math = 0

if A % C:
    no_play_day_kor += A // C + 1

else:
    no_play_day_kor += A // C

if B % D:
    no_play_day_math += B // D + 1

else:
    no_play_day_math += B // D

no_play_day = max(no_play_day_kor, no_play_day_math)

print(L - no_play_day)