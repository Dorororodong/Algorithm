list_x = []
list_y = []
list_result = []
for _ in range(3):
    a, b = map(int, input().split())
    list_x.append(a)
    list_y.append(b)

for i in list_x:
    if list_x.count(i) == 1:
        list_result.append(i)

for i in list_y:
    if list_y.count(i) == 1:
        list_result.append(i)

print(*list_result)

'''
x = []
y = []

for i in range(3):
    a,b = map(int,input().split())

    if a in x : x.remove(a)
    else : x.append(a)
    if b in y : y.remove(b)
    else : y.append(b)

print(*x,*y)
'''