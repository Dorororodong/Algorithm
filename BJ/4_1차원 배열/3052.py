my_num = []
cnt = 0

for _ in range(10):
    my_num.append(int(input()) % 42)

for i in range(42):
    if my_num.count(i) >= 1:
        cnt +=1

print(cnt)


'''
my_num = []

for _ in range(10):
    my_num.append(int(input()) % 42)

my_num = set(my_num)

print(len(my_num))
'''
