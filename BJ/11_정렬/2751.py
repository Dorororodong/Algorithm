N = int(input())

num_list = []
for _ in range(N):
    num = int(input())
    num_list.append(num)

num_list = sorted(num_list)

for i in num_list:
    print(i)