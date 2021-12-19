import sys

N = int(sys.stdin.readline())
numbers = []

for _ in range(N):
    numbers.append(int(sys.stdin.readline()))

A = round(sum(numbers) / len(numbers))
B = sorted(numbers)[len(numbers)//2]

often = []
often_num = 0
for i in numbers:
    if numbers.count(i) >= often_num:
        often_num = numbers.count(i)
        often.append(i)

C = sorted(often)[1]
D = max(numbers) - min(numbers)

print(A)
print(B)
print(C)
print(D)