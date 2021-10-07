s = input()

for i in range(97, 123):
    if chr(i) in s:
        print(s.index(chr(i)), end=' ')
    else:
        print(-1, end=' ')

------------------------------------------------------

s = input()

find = []

for i in range(97, 123):
    if chr(i) in s:
        find.append(s.index(chr(i)))
    else:
        find.append(-1)

print(*find)