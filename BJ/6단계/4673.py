entire = [i for i in range(1, 10001)]
def d(n):
    for i in range(1, 9980):
        # 반복문 범위가 에바임 (잘 모른다는 뜻임...) [밑의 풀이가 간지남]
        if i < 10:
            if (2 * i) in entire:
                entire.remove(2 * i)
        elif i < 100:
            if (i + (i // 10) + (i % 10)) in entire:
                entire.remove(i + (i // 10) + (i % 10))
        elif i < 1000:
            if (i + (i // 100) + ((i % 100) // 10) + (i % 10)) in entire:
                entire.remove(i + (i // 100) + ((i % 100) // 10) + (i % 10))
        else:
            if (i + (i // 1000) + ((i % 1000) // 100) + ((i % 100) // 10) + (i % 10)) in entire:
                entire.remove(i + (i // 1000) + ((i % 1000) // 100) + ((i % 100) // 10) + (i % 10))

d(0)
for i in entire:
    print(i, end="\n")


'''
Array = [False] * 10001
Array[0] = True

for i in range(10001):
    for j in str(i):
        i += int(j)
    if i > 10000:
        continue
    Array[i] = True
for i in range(10001):
    if not Array[i]:
        print(i)
'''