N = int(input())

sort_list = []
for _ in range(N):
    a, b = map(int, input().split())
    sort_list.append((a, b))

sort_list.sort()

for i in sort_list:
    print(*i)