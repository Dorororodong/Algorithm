N = int(input())

num = list(map(int, input().split()))

result = 0

for i in num:
    my_list = []
    for j in range(1, i+1):
        if i % j == 0:
            my_list.append(j)
    if len(my_list) == 2:
        result += 1

print(result)