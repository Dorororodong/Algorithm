my_list = []
for _ in range(9):
    my_list.append(int(input()))

print(max(my_list))
print(my_list.index(max(my_list))+1)

# my_list = [int(input()) for _ in range(9)]
# print(max(my_list), my_list.index(max(my_list))+1)