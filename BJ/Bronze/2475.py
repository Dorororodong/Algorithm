number = list(map(int, input().split()))
code = 0

for i in number:
    code += i ** 2

print(code % 10)