N = input()

sort_list = []

for i in N:
    sort_list.append(i)

sort_list.sort(reverse=True)

for i in sort_list:
    print(i, end='')



'''
print(''.join(sorted(input())[::-1]))

print("".join(sorted(input(), reverse=True)))
'''