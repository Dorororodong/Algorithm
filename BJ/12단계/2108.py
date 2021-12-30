import sys
N = int(sys.stdin.readline().rstrip())                              # 홀수
numbers = [int(sys.stdin.readline().rstrip()) for _ in range(N)]
numbers.sort()

A = round(sum(numbers) / len(numbers))
B = numbers[len(numbers)//2]

often = []
often_num = 0
for i in set(numbers):
    if numbers.count(i) > often_num:
        often_num = numbers.count(i)
        often.clear()
        often.append(i)

    elif numbers.count(i) == often_num:
        often.append(i)

if len(often) == 1:
    C = often[0]
else:
    C = sorted(often)[1]

D = max(numbers) - min(numbers)

print(A)
print(B)
print(C)
print(D)