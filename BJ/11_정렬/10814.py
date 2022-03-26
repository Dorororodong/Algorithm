T = int(input())
result = []
for _ in range(T):
    a, b = input().split()
    result.append((a, b))

for i in sorted(result, key=lambda x: int(x[0])):
    print(*i)