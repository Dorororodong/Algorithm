a = int(input())
b = int(input())
c = int(input())

num = a * b * c
my_list = []

for i in str(num):
    my_list.append(i)

for j in range(10):
    print(my_list.count(str(j)))


# a = int(input())
# b = int(input())
# c = int(input())

# d = list(map(int, (str(a * b * c))))

# for i in range(10):
#     print(d.count(i))