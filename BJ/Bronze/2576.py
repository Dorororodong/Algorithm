import sys
odd_num = []

for _ in range(7):
    num = int(sys.stdin.readline().rstrip())

    if num % 2:
        odd_num.append(num)

if odd_num:
    print(sum(odd_num))
    print(min(odd_num))

else:
    print(-1)