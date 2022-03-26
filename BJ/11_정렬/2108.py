import sys
from collections import Counter

N = int(sys.stdin.readline().rstrip())

numbers = sorted([int(sys.stdin.readline().rstrip()) for _ in range(N)])

print(round(sum(numbers) / len(numbers)))
print(numbers[N//2])
mode = Counter(numbers).most_common()
if N != 1:
    if mode[0][1] == mode[1][1]:
        print(max(mode[0][0], mode[1][0]))
    else:
        print(mode[0][0])
else:
    print(numbers[0])
print(max(numbers) - min(numbers))