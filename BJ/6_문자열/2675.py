T = int(input())
my_list = []

for tc in range(1, T+1):
    R, S = map(str, input().split())

    my_str = ''
    for i in S:
        my_str += (i * int(R))
    
    my_list.append(my_str)

for i in my_list:
    print(i)


# t=int(input())
# for i in range(t):
#     a,b=input().split()
#     for j in b:
#         print(int(a)*j, end='')
#     print() # 개행!